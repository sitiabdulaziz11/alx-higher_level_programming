#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    """
    Lists all State objects from the database hbtn_0e_6_usa.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}' .format(
        argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    # print("Number of states:", len(states))
    
    for state in states[:1]:
        print("{}: {}" .format(state.id, state.name))
