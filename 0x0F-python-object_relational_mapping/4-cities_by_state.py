#!/usr/bin/python3

"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv


def get_cities_states(username, password, dbname):
    """lists all cities from the database hbtn_0e_4_usa"""
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db=str(dbname), charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id=states.id")
    rows = cur.fetchall()
    for row in rows:
            print(row)
    cur.close()
    db.close()

if __name__ == '__main__':
    get_cities_states(argv[1], argv[2], argv[3])
