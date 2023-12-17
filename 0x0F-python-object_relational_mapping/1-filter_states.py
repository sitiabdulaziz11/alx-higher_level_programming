#!/usr/bin/python3
"""
 script that lists all states with a name starting with N from the database.
 """
import MySQLdb
import sys

if __name__ == "__main__":

    dbs = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])

    cur = dbs.cursor()
    # cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    cur.execute("SELECT id, name FROM states WHERE name LIKE '%N' ORDER BY id")

    for rows in cur.fetchall():
        print(rows)

    dbs.close()
