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

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"user {email} already exists")
        except NoResultFound:
            hashed_password = _hashed_password(password).decode('utf-8')
            new_user = self._db.add_user(email=email, hashed_password=hashed_password)
            return new_user
