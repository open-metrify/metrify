"""..."""

from pprint import pprint

from flask import current_app
from metrify import apscheduler
from metrify.github.auth.strategies import authenticate as authenticate_strat


@apscheduler.task(
    "interval", id="github.authenticate", seconds=5, misfire_grace_time=900
)
def authenticate() -> None:
    """..."""
    with apscheduler.app.app_context():
        config = current_app.config
        print(
            (authenticate_strat(config["GITHUB_CLIENT_ID"], config["GITHUB_API_KEY"]))
        )
