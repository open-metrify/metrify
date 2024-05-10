"""
The "routes.py" module registers the operation URL endpoints to the package's
`Blueprint` object.
"""

from flask import Response, jsonify

from metrify.hello import bp
from metrify.hello.operations import hello as op


@bp.route("/hello")
def hello() -> Response:
    """Status Code 200 HELLO, WORLD!"""
    return jsonify(op())
