#!/usr/bin/python3

"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv


def get_cities_states(username, password, dbname):
    """lists all cities from the database hbtn_0e_4_usa"""
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db=str(dbname), charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states\
    ON states.id = cities.state_id WHERE states.name = %s", [argv[4]])
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()

if __name__ == '__main__':
    get_cities_states(argv[1], argv[2], argv[3])
    