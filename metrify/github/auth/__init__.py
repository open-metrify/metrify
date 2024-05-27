"""
metrify/issues/__init__.py
"""

from flask import Blueprint

bp = Blueprint("github-auth", __name__)

# pylint: disable=wrong-import-position, cyclic-import
from metrify.github.auth import jobs

__all__ = ["jobs"]
