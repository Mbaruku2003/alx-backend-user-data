#!/usr/bin/python3
"""Define a class for authentication."""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """User model for the users table."""

    __tablename__: str == 'users'


    id: Column = Column(Integer, primary_key=True, nullable=False)
    email: Column = Column(String(250), nullable=False)
    hashed_password: Column = Column(String(250), nullable=False)
    session_id: Column = Column(String(250), nullable=True)
    reset_token: Column = Column(String(250), nullable=True)
