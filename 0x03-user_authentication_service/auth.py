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

class Auth:
    """Auth class to interact with the authentication database."""
    def __init__(self):
        self._db = DB()

    def register_user(email: str, password:str) -> User:
        """registers a user with the email and password."""

        if user hasattr(email):
            raise ValueError("user {user.email} already exists.""")
        else:
            _hash_password(password)
            self._db = DB()
            return User
