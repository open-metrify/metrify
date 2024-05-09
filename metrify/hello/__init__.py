"""
The `hello` package serves the sole purpose of demonstrating good 
practices and design patterns that should be enforced in the project's 
code and structuring.

This module exports a `Blueprint` object with a single registered route,
and contains an "operations.py" file, which serves as a "backend" for
the exposed endpoint.
"""

from flask import Blueprint

bp = Blueprint("hello", __name__)

# pylint: disable=wrong-import-position, cyclic-import
from metrify.hello import routes
