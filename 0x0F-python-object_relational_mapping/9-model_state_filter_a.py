#!/usr/bin/python3
"""
script that lists all State objects that contain the
letter a from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}' .format(
        argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=eng)
    sessn = Session()

    a_states = sessn.query(State).filter(State.name.like('%a%')).order_by(
            State.id).all()

    for state in a_states:
        print("{}: {}".format(state.id, state.name))

    sessn.close()
