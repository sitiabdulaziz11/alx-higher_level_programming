#!/usr/bin/python3
"""
script that takes the name of a state as an argument
and lists all cities of that state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connectmsql server"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cu = db.cursor()

    cu.execute("SELECT cities.id, cities.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        WHERE states.name LIKE BINARY %(state_name)s \
        ORDER BY cities.id ASC", {'state_name': argv[4]})

    rw = cu.fetchall()
    if rw is not None:
        print(", ".join([row[1] for row in rw]))
