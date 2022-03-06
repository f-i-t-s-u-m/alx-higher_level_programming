#!/usr/bin/python3
"""
update state id = 2
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

    q = session.query(State).filter(State.id == 2).first()
    q.name = 'New Mexico'
    session.commit()
