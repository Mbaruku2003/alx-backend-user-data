#!/usr/bin/env python3
"""Define a class for authentication."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    """User model for the users table."""

    __tablename__: str == 'users'


    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    hashed_password = Column(String(250))
    session_id = Column(String(250))
    reset_token = Column(String(250))
