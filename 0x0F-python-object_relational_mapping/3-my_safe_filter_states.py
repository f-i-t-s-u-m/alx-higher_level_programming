#!/usr/bin/python3
"""
safe ilter states by user inputs
"""


if '__main__' == __name__:
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cur = db.cursor()
    q = "SELECT * FROM states WHERE name=%s ORDER BY states.id ASC"
    cur.execute(q, (argv[4],))
    rows = cur.fetchall()
    for data in rows:
        print(data)
