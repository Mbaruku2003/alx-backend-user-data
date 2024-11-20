#!/usr/bin/env python3
"""takes in a password and returns bytes."""
import bcrypt
import uuid
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound
import typing


def _hash_password(password: str) -> bytes:
    """defined the hashed password returning bytes."""

    salted_password = bcrypt.gensalt()
    encoded_password = bcrypt.hashpw(password.encode('utf-8'), salted_password)
    return encoded_password


class Auth:
    """Auth class to interact with authentication database.
    """

    def __init__(self):
        """Initialize the Auh instance with a DB instance."""

        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user by email and passwrd."""

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        hashed_password = _hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(email: str, password: str) -> User:
        """expects email and pasword giving back a boolean."""

        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        except NoResultFound:
            pass
        return False

    def _generate_uuid() -> str:
        """Generate a new uuid."""

        return str(uuid.uuid4())
