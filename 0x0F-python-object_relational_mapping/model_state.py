#!/usr/bin/python3
"""[This python file that containcs the class definition
    of a state and an instance of Base = declarative_base()]
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """[This is the class that holds the states table]

    Args:
        Base ([object]): [new Base from which mapped classes should inherit]
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
