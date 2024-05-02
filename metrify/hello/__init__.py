from flask import Blueprint, jsonify

bp = Blueprint("hello", __name__)


@bp.route("/hello")
def hello():
    return jsonify("Hello, World!")
