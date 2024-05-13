"""..."""

from flask import Blueprint

bp = Blueprint("issues", __name__)

# pylint: disable=wrong-import-position, cyclic-import
from metrify.issues import jobs
