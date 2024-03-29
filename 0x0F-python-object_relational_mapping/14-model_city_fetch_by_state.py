#!/usr/bin/python3

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    query = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in query:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
