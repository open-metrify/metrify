"""
This module contains a function that generates a JSON Web Token (JWT) for
authenticating with the GitHub API.
"""

from time import time

from jwt import JWT, jwk_from_pem


def generate_jwt(client_id: int, pem_path: str, expiration_time: int) -> str:
    """
    Generates a JSON Web Token (JWT) for authenticating with the GitHub API.
    """

    with open(pem_path, "rb") as pem_file:
        signing_key = jwk_from_pem(pem_file.read())

    payload = {
        "iat": int(time()),
        "exp": int(time()) + expiration_time,
        "iss": client_id,
    }

    return JWT().encode(payload, signing_key, alg="RS256")


__all__ = ["generate_jwt"]
