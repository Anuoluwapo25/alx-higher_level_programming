#!/usr/bin/env python3

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    mydata = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    curobj = mydata.cursor()

    query = "SELECT * FROM states ORDER BY 'id' ASC"
    curobj.execute(query)

    states = curobj.fetchall()

    for rows in states:
        print(rows)

    curobj.close()
    mydata.close()
