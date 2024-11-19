#!/usr/bin/env python3
"""takes in a password and returns bytes."""
import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """defined the hashed password returning bytes."""

    salted_password = bcrypt.gensalt()
    encoded_password = bcrypt.hashpw(password.encode('utf-8'), salted_password)
    return encoded_password
