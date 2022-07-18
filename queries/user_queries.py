 # def test_query(message_text : str):
 #     print(f'Запрос по {message_text}')

import mysql.connector
from mysql.connector import errorcode, CMySQLConnection, MySQLConnection
from config import sqlconfig

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
    model = 'm501'
    cursor = cnx.cursor()
    sql_big_select = ('SET SQL_BIG_SELECTS = 1')
    query = ('SELECT tb_stock.sp_id, tb_stock.partno, tb_stock.partname, tb_stock.brand, tb_stock.qty, '
             'tb_models.model, tb_rate.rate, tb_price.price FROM tb_stock LEFT JOIN tb_models ON tb_stock.sp_id = '
             'tb_models.sp_id LEFT JOIN tb_rate ON tb_stock.sp_id = tb_rate.sp_id LEFT JOIN tb_price ON '
             f'tb_stock.sp_id = tb_price.sp_id WHERE tb_models.model = "{model}" GROUP BY tb_stock.sp_id ORDER BY '
             'tb_rate.rate ASC')
    cursor.execute(sql_big_select)
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    cnx.close()
