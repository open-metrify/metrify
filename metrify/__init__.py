"""
Contains initialization code for the application
"""

from flask import Flask
from flask_pymongo import PyMongo
from flask_apscheduler import APScheduler
from metrify.config import Config

mongo: PyMongo = PyMongo()
apscheduler: APScheduler = APScheduler()


def create_app(config_class: type[Config] = Config) -> Flask:
    """Metrify Flask Application Factory"""
    app: Flask = Flask(__name__)
    app.config.from_object(config_class)

    mongo.init_app(app)
    apscheduler.init_app(app)

    # pylint: disable=import-outside-toplevel, wrong-import-position
    from metrify.hello import bp as hello_bp

    app.register_blueprint(hello_bp)

    # pylint: disable=import-outside-toplevel, wrong-import-position
    from metrify.issues import bp as issues_bp

    app.register_blueprint(issues_bp)

    apscheduler.start()

    return app
