#!/usr/bin/python3
"""list State objects from a database """
from sys import argv
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]} \
        @localhost/{argv[3]}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City)
    for row in rows:
        print(f'{row.id}: {row.name} -> {row.state.name}')
    session.close()
