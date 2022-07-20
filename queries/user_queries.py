import mysql.connector
from mysql.connector import errorcode, CMySQLConnection, MySQLConnection
from config import sqlconfig


def sp_query(message_text: str):
    print(f'Запрос по {message_text}')
    try:
        cnx = mysql.connector.connect(**sqlconfig)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        model = message_text
        cursor = cnx.cursor()
        sql_big_select = ('SET SQL_BIG_SELECTS = 1')
        query = (f'SELECT tb_models.sp_id, tb_models.model, tb_models.partno, tb_models.partname, tb_models.brand, '
                 f'tb_stock.qty, tb_rate.rate, tb_price.price FROM tb_models LEFT JOIN tb_stock ON tb_models.sp_id = '
                 f'tb_stock.sp_id LEFT JOIN tb_rate ON tb_models.sp_id = tb_rate.sp_id LEFT JOIN tb_price ON '
                 f'tb_models.sp_id = tb_price.sp_id WHERE tb_models.model LIKE "%{model}%" GROUP BY tb_models.sp_id '
                 f'ORDER BY tb_rate.rate ASC')
        cursor.execute(sql_big_select)
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()
        cnx.close()
        return result
