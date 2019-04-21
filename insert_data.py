import mysql.connector
import csv
mysql = mysql.connector.connect(host="localhost", user = "root", password = "32461997", database = "Spy")
cursor = mysql.cursor(buffered=True)

#Spy.AGENT
insert_command = ("INSERT INTO Spy.AGENT (Agent_id, Name, Status, Salary, Emergency_contact_line) VALUES (%s, %s, %s, %s, %s)")
cursor.execute("DELETE FROM Spy.AGENT")
with open("agent_list_file.csv", "r") as file:
    f = csv.reader(file)
    for i in f:
        data = list(i)
        data[0] = int(data[0])
        data[3] = int(data[3])
        data[4] = int(data[4])
        data = tuple(data)
        print(data)
        #print("\n\n")
        cursor.execute(insert_command, data)
#commit changes
mysql.commit()
