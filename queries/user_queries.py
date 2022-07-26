import mysql.connector
from mysql.connector import errorcode, CMySQLConnection, MySQLConnection
from config import sqlconfig



def short_model_query():
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
        cursor = cnx.cursor()
        shortNameQuery = (
            f'SELECT tb_models.model FROM tb_models WHERE CHAR_LENGTH(model) < 3 GROUP BY tb_models.model')
        cursor.execute(shortNameQuery)
        shortModelList = cursor.fetchall()
        shortModelrow: list = []
        for row in shortModelList:
            shortModelrow.append(row[0])
        cursor.close()
        cnx.close()
        return shortModelrow

def sp_query(model: str, shortModelList):
    print(f'Запрос по {model}')
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
        cursor = cnx.cursor()
        sql_big_select = ('SET SQL_BIG_SELECTS = 1')
        if model in shortModelList:
            queryPart = f'= "{model}"'
        else:
            queryPart = f'LIKE "%{model}%"'
        mainquery = (f'SELECT tb_models.sp_id, tb_models.model, tb_models.partno, tb_models.partname, tb_models.brand, '
                 f'tb_stock.qty, tb_rate.rate, tb_price.price FROM tb_models LEFT JOIN tb_stock ON tb_models.sp_id = '
                 f'tb_stock.sp_id LEFT JOIN tb_rate ON tb_models.sp_id = tb_rate.sp_id LEFT JOIN tb_price ON '
                 f'tb_models.sp_id = tb_price.sp_id WHERE tb_models.model {queryPart} GROUP BY tb_models.sp_id '
                 f'ORDER BY tb_rate.rate ASC')
        cursor.execute(sql_big_select)
        cursor.execute(mainquery)
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()
        cnx.close()
        return result
