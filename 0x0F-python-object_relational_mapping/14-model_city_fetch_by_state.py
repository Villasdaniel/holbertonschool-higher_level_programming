#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
from sqlalchemy import create_engine, text
from sys import argv
from sqlalchemy.orm import Session
from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    cities = session.query(State, City).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for state, city in cities:
        print("{:s}: ({:d}) {:s}".format(state.name, city.id, city.name))
    session.close()
