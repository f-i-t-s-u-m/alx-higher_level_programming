#!/usr/bin/python3
"""
select states
"""


if '__main__' == __name__:
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for data in rows:
        print(data)
