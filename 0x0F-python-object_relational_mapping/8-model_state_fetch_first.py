#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))
    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    try:
        id, name = session.query(State.id, State.name).from_statement(text(
                "SELECT id, name "
                "FROM states "
        )).first()
        print("{:d}: {:s}".format(id, name))
    except TypeError:
        print('nothing')
    session.close()
