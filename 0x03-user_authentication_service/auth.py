#!/usr/bin/env python3
"""takes in a password and returns bytes"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """define hashpasswod in bytes."""

    salt = bcrypt.gensalt()
    the_passwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return the_passwd
