"""..."""

from pprint import pprint
from flask import current_app, g
from gql import gql
from gql.transport.requests import RequestsHTTPTransport
from metrify import apscheduler, graphql
from metrify.github.auth.strategies import get_access_token as authenticate_strat
from metrify.github.utils import generate_github_jwt


@apscheduler.task(
    "interval", id="github.authenticate", seconds=10, misfire_grace_time=900
)
def authenticate() -> None:
    """
    Periodically resets the Github API access token to keep the app authenticated.
    """
    with apscheduler.app.app_context():
        config = current_app.config

        jwt = generate_github_jwt(
            config["GITHUB_CLIENT_ID"], config["GITHUB_API_KEY"], 600
        )

        access_token = authenticate_strat(jwt, config["GITHUB_INSTALLATION_ID"])

        graphql.transport = RequestsHTTPTransport(
            url="https://api.github.com/graphql",
            use_json=True,
            headers={"Authorization": "Bearer {}".format(access_token)},
        )
