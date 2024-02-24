import MySQLdb
import sys

if __name__ = "__main__":
    username, password, database = argv[1], argv[2], argv[3]

    mydata = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    curobj = mydata.cursor()

    query = "SELECT * FROM states ORDER BY id"
    curobj.execute(query)

    states = curobj.fetchall()

    for state in states:
        print(state)

        curobj.close()
        mydata.close()
