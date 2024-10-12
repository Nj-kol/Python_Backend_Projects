from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative.api import DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from .core.config import settings

SQLALCHEMY_DATABASE_URI = settings.DATABASE_URI

engine: Engine = create_engine(SQLALCHEMY_DATABASE_URI)
session_local: sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db: Session = session_local()

Base: DeclarativeMeta = declarative_base()
