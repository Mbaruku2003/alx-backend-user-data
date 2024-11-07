#!/usr/bin/env python3
"""created a new repository first file."""
import logging
import typing
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection
import re
from typing import List, Tuple


PII_FIELDS: Tuple[str, ...] = (
        "name", "email", "ssn", "password", "phone")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialisation continuation."""

        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Where i'll implement the new code."""

        record.msg = filter_datum(
                self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """Obfuscates field in a log message."""

    pattern = f"({'|'.join(fields)})=([^ {separator}]+)"
    return re.sub(pattern, f"\\1={redaction}", message)


def get_logger() -> logging.Logger:
    """returns a logging.logger object."""

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> MySQLConnection:
    """Returns a connector to a MYSQL database."""

    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    cnx = mysql.connector.connection.MySQLConnection(user=username,
                                                     password=password,
                                                     host=host,
                                                     database=db_name)
    return cnx


def main():
    """obtain the database connectin using get_db and retreive rows."""

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    field_names = [i[0] fr i in cursor.description]
    logger = get_logger()
    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, field_names))
        logger.info(str_row.strip())
    cursor.close()
    db.close()
