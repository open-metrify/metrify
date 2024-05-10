"""
Contains initialization code for the application
"""

from flask import Flask
from flask_pymongo import PyMongo
from flask_apscheduler import APScheduler
from metrify.config import Config

mongo: PyMongo = PyMongo()  # type: ignore
apscheduler: APScheduler = APScheduler()


def create_app(config_class: type[Config] = Config) -> Flask:
    """Metrify Flask Application Factory"""
    app: Flask = Flask(__name__)
    app.config.from_object(config_class)
    mongo.init_app(app)  # type: ignore
    apscheduler.init_app(app)
    apscheduler.start()

    # pylint: disable=import-outside-toplevel, wrong-import-position
    from metrify.hello import bp as hello_bp

    app.register_blueprint(hello_bp)

    return app
