"""
Exports configuration data for the Flask application
"""


class Config:
    """
    Configuration class for the Flask application.

    Should be used with `from_object`::

        config = Config
        app.config.from_object(config)
    """

    MONGO_URI = "mongodb://localhost:27017/metrify"
