#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from model_state import Base

engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ),
    pool_pre_ping=True
)

Base.metadata.create_all(engine)

