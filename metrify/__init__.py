from flask import Flask
from flask_pymongo import PyMongo

from metrify.config import Config

mongo = PyMongo()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mongo.init_app(app)

    from metrify.hello import bp as hello_bp

    app.register_blueprint(hello_bp)

    return app
