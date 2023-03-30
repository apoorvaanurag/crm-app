import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root1234'
)

#prepare cursor object

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_db")

print("ALL DONE!")