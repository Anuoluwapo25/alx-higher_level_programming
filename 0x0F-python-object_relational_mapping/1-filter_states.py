#!/usr/bin/python3

"""
    script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    mydata = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8")

    cur = mydata.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY 'id' ASC")

    states = cur.fetchall()

    for rows in states:
        if rows[0] == "N":
            print(rows)

    cur.close()
    mydata.close()
