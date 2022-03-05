#!/usr/bin/python3
"""
base model file
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ state class """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "id:{} | name:{} ".format(self.id, self.name)
