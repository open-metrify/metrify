"""..."""

from flask import Blueprint

bp = Blueprint("github-projects", __name__)

# pylint: disable=wrong-import-position, cyclic-import
from metrify.github.projects import jobs

__all__ = ["jobs"]
