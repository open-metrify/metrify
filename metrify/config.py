"""
Exports configuration data for the Flask application
"""

from dotenv import dotenv_values

env = dotenv_values(".env")


class Config:
    """
    Configuration class for the Flask application.

    Should be used with `from_object`::

        config = Config
        app.config.from_object(config)
    """

    SCHEDULER_API_ENABLED = True

    MONGO_URI = "mongodb://localhost:27017/metrify"

    GITHUB_CLIENT_ID = env["APP_ID"]
    GITHUB_API_KEY = env["PRIVATE_KEY_PATH"]
