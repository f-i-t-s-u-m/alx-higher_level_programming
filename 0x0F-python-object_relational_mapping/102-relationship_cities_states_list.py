#!/usr/bin/python3
"""
sqlalchemy one to many relation
"""


if __name__ == '__main__':

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import Base, State
    from sys import argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City)

    for city in query:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
