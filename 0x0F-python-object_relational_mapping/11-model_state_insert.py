#!/usr/bin/python3
"""
lists all State objects from the database in ascending order
using SQLAlchemy and importing State and Base from model_state
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    state_name = (State(id=6, name='Louisiana'))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(state_name)
    session.commit()
    print("{}".format(state_name.id))
    session.close()
