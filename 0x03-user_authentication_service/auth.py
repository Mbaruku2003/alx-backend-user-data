#!/usr/bin/env python3
"""takes in a password and returns bytes"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """define hashpasswod in bytes."""

    salted_PASWD = bcrypt.gensalt(password)
    the_passwd = bcrypt.encode(encoding="UTF-8", salted_PASWD)
    return the_passwd
