#!/usr/bin/python3
"""
a python file that contains the class definition of a State and
an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class:
            -it inherits from Base
            -should represent a table called states in MySQL db

        Attributes:
            __tablename__ = 'states' table name
            id(int)
            name(str)
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # engine = create_engine('mysql://argv[1]:argv[2]@localhost:3306/argv[3]')
