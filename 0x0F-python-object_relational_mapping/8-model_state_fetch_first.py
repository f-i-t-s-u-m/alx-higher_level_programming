#!/usr/bin/python3
"""
fetch state using sqlalchemy
"""


if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sys import argv
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).first()
    if row:
        print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")
