import mysql.connector
import csv
mysql = mysql.connector.connect(host="localhost", user = "root", password = "32461997")
cursor = mysql.cursor(buffered=True)

#open and read commands
with open("SPY_DB_SETUP.sql", "r") as sql:
    sqlFile = sql.read()
    sqlCommands = sqlFile.split(';')
    #for line in sqlCommands:
    #    print(line)

#cursor.execute("CREATE SCHEMA IF NOT EXISTS 'Spy' DEFAULT CHARACTER SET utf8")

#execute every sqlCommands
for command in sqlCommands:
    try:
        #print(command)
        cursor.execute(command)
    except Exception as e:
        print('error')
cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)

insert_command = "INSERT AGENT (Agent_id, Name, Status, Salary, Emergency_contact_line) VALUES(4239, 'Dat Q Ngo', 'Single', 40000, 714813)"
print(cursor.execute(insert_command))
cursor.execute("SELECT * FROM AGENT")
result = cursor.fetchall()
for x in cursor:
    print(x)
#print('hello')

file = csv.writer(open("test.csv", "w+"))
file.writerows(result)
mysql.commit()
