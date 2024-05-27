from pprint import pprint

from flask import json
from metrify.github.utils import generate_github_jwt
import requests


def get_access_token(jwt: str, installation_id: str) -> str:
    """
    Retrieves an installation access token from the Github API via an installation id and JWT.

    :param jwt: JWT generated from the Github App credentials
    :type jwt: str

    :param installation_id: Github App installation ID
    :type installation_id: str

    :return: Github installation access token
    :rtype: str
    """

    url = "https://api.github.com/app/installations/{}/access_tokens".format(
        installation_id
    )
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer {}".format(jwt),
    }
    response = requests.post(
        url,
        headers=headers,
    )

    # TODO: handle errors

    return json.loads(response.content)["token"]
