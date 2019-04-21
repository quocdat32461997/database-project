import mysql.connector
import csv
mysql = mysql.connector.connect(host="localhost", user = "root", password = "32461997")
cursor = mysql.cursor(buffered=True)

#open and read commands
with open("SPY_DB_SETUP.sql", "r") as sql:
    sqlFile = sql.read()
    sqlCommands = sqlFile.split(';')

#execute every sqlCommands
for command in sqlCommands:
    try:
        cursor.execute(command)
    except Exception as e:
        print('error')

#check if database is created
cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)

#commit changes
mysql.commit()
