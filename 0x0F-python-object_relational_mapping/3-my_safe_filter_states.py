#!/usr/bin/python3

"""lists all states with a name starting with N (upper N) from the database"""

import MySQLdb
from sys import argv


def get_states(username, password, dbname, match):
    """lists all states with a name starting with N from the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db=str(dbname), charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%(name)s", {'name': match})
    rows = cur.fetchall()
    for row in rows:
            print(row)
    cur.close()
    db.close()

if __name__ == '__main__':
        get_states(argv[1], argv[2], argv[3], argv[4])
