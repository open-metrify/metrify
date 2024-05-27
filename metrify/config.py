"""
metrify/config.py

Exports configuration data for the Flask application
"""

from dotenv import dotenv_values

env = dotenv_values(".env")


class Config:
    """
    Configuration class for the Flask application.

    :note: Should be used with `from_object`

    :example:
        >>> config = Config
        >>> app.config.from_object(config)

    :ivar MONGO_URI: URI for the MongoDB connection
    :vartype MONGO_URI: str

    :ivar SCHEDULER_API_ENABLED: APScheduler-enabled API integration
    :vartype SCHEDULER_API_ENABLED: bool
    """

    SCHEDULER_API_ENABLED = True

    MONGO_URI = "mongodb://localhost:27017/metrify"

    GITHUB_CLIENT_ID = env["APP_ID"]
    GITHUB_INSTALLATION_ID = env["INSTALLATION_ID"]
    GITHUB_API_KEY = env["PRIVATE_KEY_PATH"]
