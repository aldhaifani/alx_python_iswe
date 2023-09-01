#!/usr/bin/python3
"""
a script that prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )

    factory = sessionmaker(bind=engine)
    session = factory()

    try:
        first_state = session.query(State)[0]
        print("{}: {}".format(first_state.id, first_state.name))
    except IndexError:
        print("Nothing")
