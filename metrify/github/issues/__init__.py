"""..."""

from flask import Blueprint

bp = Blueprint("github-issues", __name__)

# pylint: disable=wrong-import-position, cyclic-import
from metrify.github.issues import jobs

__all__ = ["jobs"]
