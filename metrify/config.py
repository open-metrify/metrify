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

    :ivar GITHUB_CLIENT_ID: Client ID for the Github App integration
    :vartype GITHUB_CLIENT_ID: str

    :ivar GITHUB_INSTALLATION_ID: App installation ID for the Github App
        integration
    :vartype GITHUB_INSTALLATION_ID: str

    :ivar GITHUB_API_KEY_PEM: Path to the `.pem` file containing the private
        key to the Github App
    :vartype GITHUB_API_KEY_PEM: str
    """

    SCHEDULER_API_ENABLED = True
    MONGO_URI = "mongodb://localhost:27017/metrify"
    GITHUB_CLIENT_ID = env.get("APP_ID", "")
    GITHUB_INSTALLATION_ID = env.get("INSTALLATION_ID", "")
    GITHUB_API_KEY_PEM = env.get("PRIVATE_KEY_PATH", "")
