#!/usr/bin/python3
"""
List all cities of state
"""


if '__main__' == __name__:
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cur = db.cursor()
    q = """ SELECT cities.name FROM cities INNER JOIN states
        ON states.id = state_id WHERE states.name = %s"""
    cur.execute(q, (argv[4],))
    print(", ".join(i[0] for i in cur.fetchall()))
