#!/usr/bin/python3
"""
safe ilter states by user inputs
"""


if '__main__' == __name__:
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cur = db.cursor()
    q = """SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states ON state_id = states.id
        ORDER BY cities.id ASC"""
    cur.execute(q)
    rows = cur.fetchall()
    for data in rows:
        print(data)
