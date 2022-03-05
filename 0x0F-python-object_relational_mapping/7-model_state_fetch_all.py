#!/usr/bin/python3
"""
fetch state using sqlalchemy
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
import pymysql
if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State).order_by(State.id):
        print("{}: {}".format(i.id, i.name))
