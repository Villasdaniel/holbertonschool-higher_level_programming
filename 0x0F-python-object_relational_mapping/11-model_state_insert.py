#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    session = Session(engine)
    stad = State(name="Louisiana")
    session.add(stad)
    session.commit()
    print("{}".format(stad.id))
    session.close()
