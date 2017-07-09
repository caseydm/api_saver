import os
from sqlalchemy import create_engine, Column, DateTime, func, Integer, JSON, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database configuration
engine = create_engine(os.environ['DATABASE_URL'])
Base = declarative_base()
Session = sessionmaker(bind=engine)


# models
class Post(Base):
    """Post model."""
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer)
    title = Column(String(200))
    body = Column(String)
    last_updated = Column(DateTime, server_default=func.now())


class PostJSON(Base):
    """Post JSON model."""
    __tablename__ = 'posts_json'

    id = Column(Integer, primary_key=True)
    data = Column(JSON)
    last_updated = Column(DateTime, server_default=func.now())


# create tables
Base.metadata.create_all(engine)
