from flask import Blueprint

bp = Blueprint("hello", __name__)

from metrify.hello import routes
