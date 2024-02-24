import MySQLdb
import sys


mydata = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

curobj = mydata.cursor()

query = "SELECT * FROM states ORDER BY id"
cursor.execute(query)

states = cursor.fetchall()


for state in states:
    print(state)

cursor.close()
mydata.close()
