"""
metrify/github/utils/__init__.py

This module exports utility functions for integrating with the Github API.
"""

from time import time

from jwt import JWT, jwk_from_pem

from metrify.exception import InvalidArgumentError


def generate_github_jwt(
    client_id: str, pem_path: str, expiration_time: int = 600
) -> str:
    """
    Generates a JSON Web Token (JWT) for authenticating as a GitHub App from
    client ID and PEM file.

    :param client_id: Client ID for the Github App
    :type client_id: str

    :param pem_path: Path to the PEM file containing a private key for the
        Github App.
    :type pem_path: str

    :param expiration_time: Expiration time for the JWT, in seconds; 600 second
        maximum limit.
    :type expiration_time: int

    :return: JWT to authenticate the Github App
    :rtype: str

    :raises FileNotFoundError: if path specified for PEM file is invalid
    :raises UnsupportedKeyTypeError: if private key is invalid
    :raises InvalidArgumentError: if `expiration_time` argument is grater than
        600 seconds
    """

    if expiration_time > 600:
        raise InvalidArgumentError(
            """
Maximum expiration time for Github App tokens is 600 seconds (10 minutes)"""
        )

    with open(pem_path, "rb") as pem_file:
        signing_key = jwk_from_pem(pem_file.read())

    payload = {
        "iat": int(time()),
        "exp": int(time()) + expiration_time,
        "iss": client_id,
    }

    return JWT().encode(payload, signing_key, alg="RS256")


__all__ = ["generate_github_jwt"]
