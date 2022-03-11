import pymysql

db = pymysql.connect( 
    host='localhost', 
    port=3306, user='root', 
    password='admin123', 
    database='pruebitas_flask')