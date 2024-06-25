"""
Test suite for metrify.github.utils
"""

from typing import Generator
from unittest.mock import MagicMock, patch, mock_open
from jwt import JWT
from jwt.exceptions import UnsupportedKeyTypeError
from pytest import raises

import pytest

from metrify.exception import InvalidArgumentError
from metrify.github.utils import generate_github_jwt


class TestGenerateGithubJwt:
    """Test suite for `generate_github_jwt` function"""

    @pytest.fixture(scope="class")
    def data(self) -> Generator[tuple, None, None]:
        """Setup and Teardown"""

        client_id = "test_client_id"
        pem_path = "test_path.pem"
        expiration_time = 600
        yield client_id, pem_path, expiration_time

    @patch("metrify.github.utils.jwk_from_pem")
    @patch("metrify.github.utils.time")
    def test_generate_success(
        self, mock_time: MagicMock, mock_jwk: MagicMock, data: tuple
    ):
        """
        Should correctly make calls to generate, encode, and return the JWT
        """

        client_id, pem_path, expiration_time = data

        private_key = (
            "-----BEGIN PRIVATE KEY-----\n"
            + "MIIEvgIBADANBgkqhkiG9w0BAQEFAASC\n"
            + "-----END PRIVATE KEY-----"
        )
        pem_contents = private_key.encode("utf-8")
        signing_key = "test_jwk"
        encode_result = "test_jwt_token"

        mock_time.return_value = 1000
        mock_jwk.return_value = signing_key

        with patch("builtins.open", mock_open(read_data=pem_contents)) \
                as mock_open_file:
            with patch.object(JWT, "encode", return_value=encode_result) \
                    as mock_encode:
                result = generate_github_jwt(
                    client_id,
                    pem_path,
                    expiration_time
                )

                mock_open_file.assert_called_once_with(pem_path, "rb")
                mock_jwk.assert_called_once_with(pem_contents)
                mock_encode.assert_called_once_with(
                    {
                        "iat": 1000,
                        "exp": 1600,
                        "iss": client_id,
                    },
                    signing_key,
                    alg="RS256",
                )
                assert result == encode_result

    @patch("metrify.github.utils.jwk_from_pem")
    @patch("metrify.github.utils.time")
    @patch("builtins.open")
    def test_not_found(
        self,
        mock_open_file: MagicMock,
        mock_time: MagicMock,
        mock_jwk: MagicMock,
        data: tuple,
    ):
        """
        Should halt execution and return 'None' in case an invalid PEM path is
        passed to the function
        """

        client_id, pem_path, expiration_time = data

        mock_open_file.side_effect = FileNotFoundError

        with raises(FileNotFoundError):
            with patch.object(JWT, "encode") as mock_encode:
                result = generate_github_jwt(
                    client_id,
                    pem_path,
                    expiration_time
                )
                mock_open_file.assert_called_once_with(pem_path, "rb")
                mock_jwk.assert_not_called()
                mock_time.assert_not_called()
                mock_encode.assert_not_called()
                assert result is None

    @patch("metrify.github.utils.jwk_from_pem")
    @patch("metrify.github.utils.time")
    def test_invalid_key(
            self,
            mock_time: MagicMock,
            mock_jwk: MagicMock,
            data: tuple):
        """
        Should halt execution and return 'None' in case an invalid PEM file is
        passed to the function
        """

        client_id, pem_path, expiration_time = data

        pem_contents = b"invalid_key_data"

        mock_jwk.side_effect = UnsupportedKeyTypeError

        with patch(
            "builtins.open", mock_open(read_data=pem_contents)
        ) as mock_open_file:
            with raises(UnsupportedKeyTypeError):
                with patch.object(JWT, "encode") as mock_encode:
                    result = generate_github_jwt(
                        client_id,
                        pem_path,
                        expiration_time
                    )
                    mock_open_file.assert_called_once_with(pem_path, "rb")
                    mock_jwk.assert_called_once_with(pem_contents)
                    mock_encode.assert_not_called()
                    mock_time.assert_not_called()
                    assert result is None

    @patch("metrify.github.utils.jwk_from_pem")
    @patch("metrify.github.utils.time")
    @patch("builtins.open")
    def test_invalid_expiration(
        self,
        mock_open_file: MagicMock,
        mock_time: MagicMock,
        mock_jwk: MagicMock,
        data: tuple,
    ):
        """
        Should halt execution and return 'None' in case an invalid execution
        time parameter is passed to the function
        """

        client_id, pem_path, *_ = data

        expiration_time = 601

        with raises(InvalidArgumentError):
            with patch.object(JWT, "encode") as mock_encode:
                result = generate_github_jwt(
                    client_id, pem_path, expiration_time)
                mock_open_file.assert_not_called()
                mock_jwk.assert_not_called()
                mock_time.assert_not_called()
                mock_encode.assert_not_called()
                assert result is None
