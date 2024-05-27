"""
metrify/__init__.py

Contains initialization code for the application
"""

from flask import Flask
from flask_pymongo import PyMongo
from flask_apscheduler import APScheduler
from metrify.config import Config
from gql import Client
import os

with open("{}/graphql/github.schema.graphql".format(os.path.dirname(__file__))) as f:
    github_schema = f.read()

client = Client(schema=github_schema)
mongo: PyMongo = PyMongo()
""":class:`PyMongo`: An instance of the database client class used to interact with the database."""

apscheduler: APScheduler = APScheduler()
""":class:`APScheduler`: An instance of the Advanced Python Scheduler class
used to set events to be periodically executed."""


def create_app(config_class: type[Config] = Config) -> Flask:
    """
    Metrify Flask Application Factory

    :param config_class: Config class for the Flask application
    :type config_class: type :class:`metrify.config.Config`

    :return: The Flask application instance
    :rtype: :class:`Flask`
    """

    app: Flask = Flask(__name__)
    app.config.from_object(config_class)

    mongo.init_app(app)
    apscheduler.init_app(app)

    # pylint: disable=import-outside-toplevel, wrong-import-position
    from metrify.hello import bp as hello_bp

    app.register_blueprint(hello_bp)

    # pylint: disable=import-outside-toplevel, wrong-import-position
    from metrify.github.issues import bp as github_issues_bp

    app.register_blueprint(github_issues_bp)

    # pylint: disable=import-outside-toplevel, wrong-import-position
    from metrify.github.auth import bp as github_auth_bp

    app.register_blueprint(github_auth_bp)

    apscheduler.start()

    return app

__all__ = ["client", "mongo", "apscheduler", "create_app"]
