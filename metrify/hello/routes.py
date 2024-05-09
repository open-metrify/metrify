from flask import jsonify

from metrify.hello import bp
from metrify.hello.operations import hello as op


@bp.route("/hello")
def hello():
    return jsonify(op())
