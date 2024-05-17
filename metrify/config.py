"""
metrify/config.py

Exports configuration data for the Flask application
"""


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

    MONGO_URI = "mongodb://localhost:27017/metrify"
    SCHEDULER_API_ENABLED = True
