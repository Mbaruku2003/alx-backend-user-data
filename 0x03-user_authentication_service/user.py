#!/usr/bin/env python3
"""Define a way to know a user."""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from typing import Any, Type


Base = declarative_base()


class User(Base):  # type: ignore
    """define table user to be used."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
