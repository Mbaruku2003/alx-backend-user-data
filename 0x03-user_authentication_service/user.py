#!/usr/bin/env python3
"""Define a way to know a user."""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import typing
from typing import Column


Base = declarative_base()

class User(Base):
    """define table user"""

    __tablename__ = "user"

    id = Column(Integer, AutoIncrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

