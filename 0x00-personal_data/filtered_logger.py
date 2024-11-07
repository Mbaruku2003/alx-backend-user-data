#!/usr/bin/env python3
"""created a new repository first file."""
import logging
import typing
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
