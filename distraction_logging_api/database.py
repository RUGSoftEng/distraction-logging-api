"""
    Creates the database. 
    For information about how to access the database via a session-variable, see: session_scope() 
"""

from sqlalchemy import Column, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager

# when using a different database, use another database_name
database_name = 'sqlite:///database.db'
Base = declarative_base()


class Log(Base):
    """ Table for storing the log information """
    __tablename__ = 'log'
    id = Column(String(250), primary_key=True) #Primary key, see dbSize in main.py
    userID = Column(String(250), nullable=False) #ID corresponding to users. Generated for each user and sent from extension
    trigger = Column(String(250), nullable=False) #Which user action was made
    event = Column(String(250), nullable=False) #What the user did, modified/added/intercepted etc
    value = Column(String(250), nullable=False) #The value of the event, eg user changed slider to value: 56
    time = Column(String(250), nullable=False) #Time of event
    type = Column(String(250), nullable=False) #Type of event, settings/statistics etc


# create the database
engine = create_engine(database_name)

# creates all tables in the database
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """
    When accessing the database, use the following syntax:
        with session_scope() as db_session:
            db_session.query(...)
            
    :return: the session for accessing the database
    """
    session = DBSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
