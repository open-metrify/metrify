"""
metrify/exception/__init__.py

This module exports application-related custom exceptions.
"""


class ContextException(Exception):
    """
    Exception relating to the Flask app context.
    """

    def __str__(self) -> str:
        return """
Invalid call to context-related resources while working outside of Flask application context"""


__all__ = ["ContextException"]
