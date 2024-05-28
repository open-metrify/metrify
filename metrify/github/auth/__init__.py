"""
metrify/github/auth/__init__.py

The `auth` package implements the scheduling and backend routine functions to
keep the application properly connected and authenticated to the Github API in
order to execute queries via the global GraphQL client.
"""

from flask import Blueprint

bp = Blueprint("github-auth", __name__)

# pylint: disable=wrong-import-position, cyclic-import
from metrify.github.auth import jobs

__all__ = ["jobs"]
