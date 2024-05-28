"""
metrify/github/auth/jobs.py

The "jobs.py" module registers the scheduler-operated routines to the
application's global :class:`APScheduler` instance.
"""

from flask import current_app
from gql.transport.requests import RequestsHTTPTransport
from metrify import apscheduler, graphql
from metrify.exception import ContextException
from metrify.github.auth.strategies import get_access_token as authenticate_strat
from metrify.github.utils import generate_github_jwt


@apscheduler.task(
    "interval", id="github.authenticate", seconds=10, misfire_grace_time=900
)
def authenticate() -> None:
    """
    Periodically resets the Github API access token to keep the app authenticated.

    :raises ContextException: if app context is not accessible from scheduler instance
    """
    if apscheduler.app is None:
        raise ContextException(
            "APScheduler instance is not linked to Flask application"
        )

    with apscheduler.app.app_context():
        config = current_app.config

        jwt = generate_github_jwt(
            config["GITHUB_CLIENT_ID"], config["GITHUB_API_KEY"], 540
        )

        access_token = authenticate_strat(
            jwt, config["GITHUB_INSTALLATION_ID"])

        graphql.transport = RequestsHTTPTransport(
            url="https://api.github.com/graphql",
            use_json=True,
            headers={"Authorization": f"Bearer {access_token}"},
        )
