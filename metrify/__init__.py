"""
metrify/__init__.py

Contains initialization code for the application
"""


import os
import json
import atexit
import logging.config
import logging.handlers
from pathlib import Path
from flask import Flask
from flask_pymongo import PyMongo
from flask_apscheduler import APScheduler
from gql import Client

from metrify.config import Config

cwd = os.path.dirname(__file__)

with open(f"{cwd}/log/config.json", encoding="utf-8") as log_c:
    logger_config = json.load(log_c)
    file_out = logger_config["handlers"]["file"]["filename"]
    logger_config["handlers"]["file"]["filename"] = file_out.format(
        path=Path(cwd).parent.absolute()
    )
    logging.config.dictConfig(logger_config)
    queue_handler = logging.getHandlerByName("queueHandler")
    if queue_handler is not None:
        queue_handler.listener.start()  # type: ignore[attr-defined]
        atexit.register(
            queue_handler.
            listener.stop               # type: ignore[attr-defined]
        )

with open(f"{cwd}/graphql/github.schema.graphql", encoding="utf-8") as gql_c:
    github_schema = gql_c.read()

logger = logging.getLogger(__name__)
""":class:`Logger`: The Logger instance for the application."""

graphql = Client(
    schema=github_schema,
)
""":class:`Client`: An instance of the GraphQL client class used to interact
with the Github API."""

mongo: PyMongo = PyMongo()
""":class:`PyMongo`: An instance of the database client class used to interact
with the database."""

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


__all__ = ["graphql", "mongo", "apscheduler", "create_app", "logger"]
