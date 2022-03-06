#!/usr/bin/python3
"""
List all state containing letter a
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
            argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State).filter(State.name==argv[4]):
        print("{}".format(i.id))
