#!/usr/bin/python3
"""
script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where
name matches the argument.
and
that is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    try:
        dbs = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3])

        cr = dbs.cursor()

        cr.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
                ORDER BY states.id ASC", (argv[4],))

        for row in cr.fetchall():
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if dbs:
            dbs.close()
