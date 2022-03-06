#!/usr/bin/python3
"""
sqlalchemy one to many relation
"""


if __name__ == '__main__':
    
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City
    from sys import argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cal = State(name='California')
    san = City(name='San Francisco', state=cal)
    session.add(san)
    session.commit()
