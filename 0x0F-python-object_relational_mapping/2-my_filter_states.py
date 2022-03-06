#!/usr/bin/python3
"""
filter states by user inputs
"""


if '__main__' == __name__:
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"
                .format(argv[4]))
    rows = cur.fetchall()
    for data in rows:
        print(data)
