#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import insert
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    stateColumn = session.query(State).filter(State.name.like('%a%')).all()
    for state in stateColumn:
        if "a" in state.name:
            session.delete(state)

    session.commit()

    session.close()
