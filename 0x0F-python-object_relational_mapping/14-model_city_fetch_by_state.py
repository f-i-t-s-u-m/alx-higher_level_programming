#!/usr/bin/python3
"""
list cities
"""


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_city import Base, City
    from model_state import State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({}) {}".format(i.State.name, i.City.id, i.City.name))
