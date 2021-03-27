#!/usr/bin/python3
"""[This is a file fimilar to model_state]
"""
from model_state import Base, State
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """[This inherts from base]

    Args:
        Base ([obj]): [This is the ]
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state_id'), nullable=False)
