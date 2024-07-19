"""
metrify/github/auth/strategies.py

The "strategies.py" module implements the "backend" for the scheduled jobs
registered by the package's "jobs.py".
"""

from flask import json
import requests


def get_access_token(jwt: str, installation_id: str) -> str:
    """
    Retrieves an installation access token from the Github API via an
    installation id and JWT.

    :param jwt: JWT generated from the Github App credentials
    :type jwt: str

    :param installation_id: Github App installation ID
    :type installation_id: str

    :return: Github App installation access token
    :rtype: str
    """

    url = f"https://api.github.com/app/installations/{
        installation_id}/access_tokens"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {jwt}",
    }
    response = requests.post(
        url,
        headers=headers,
        timeout=10,
    )

    # pylint: disable=fixme
    # TODO: handle errors

    # pylint: disable=fixme
    # TODO: remover cast desnecessário aqui quando incluir pydantic e modelos
    # de dados da API
    return str(json.loads(response.content)["token"])
