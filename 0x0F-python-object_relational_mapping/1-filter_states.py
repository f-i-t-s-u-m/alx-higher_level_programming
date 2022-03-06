#!/usr/bin/python3
"""
select states
"""


if '__main__' == __name__:
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cur = db.cursor()
    q = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cur.execute(q)
    rows = cur.fetchall()
    for data in rows:
        if data[1].startswith('N'):
            print(data)
