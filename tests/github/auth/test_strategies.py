"""
Test suite for metrify.github.auth.strategies
"""

from sys import path
from typing import Any, Generator, Tuple
from unittest.mock import MagicMock, patch
from pytest import raises
import pytest

from requests import RequestException

from metrify.github.auth.model import AuthResponse
from metrify.github.auth.strategies import get_access_token

type Fixture = Tuple[Any, Any, Any, Any, Any]


class TestGetAccessToken:
    """Test suite for `get_access_token` function"""

    @pytest.fixture(scope="class")
    def data(self) -> Generator[Fixture, None, None]:
        """Setup and Teardown"""

        jwt = "test_jwt"
        installation_id = "test_installation_id"

        # pylint: disable=R0801
        url = f"https://api.github.com/app/installations/{
            installation_id}/access_tokens"
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {jwt}",
        }
        timeout = 10
        yield jwt, installation_id, url, headers, timeout

    @patch("metrify.github.auth.model.AuthResponse.model_validate_json")
    @patch("requests.post")
    def test_returns_token(
        self, mock_post: MagicMock, mock_parse: MagicMock, data: Fixture
    ) -> None:
        """
        Should correctly extract and return the 'token' attribute value from
        the response body
        """

        jwt, installation_id, url, headers, timeout = data

        token_value = "test_token"
        response_content = "{ token: { " + token_value + " } }"

        response = MagicMock()
        response.content = response_content
        mock_post.return_value = response
        mock_parse.return_value = token_value

        result = get_access_token(jwt, installation_id)

        mock_post.assert_called_once_with(url, headers=headers, timeout=timeout)
        mock_parse.assert_called_once_with(response_content)
        assert result == token_value

    @patch("metrify.github.auth.model.AuthResponse.model_validate_json")
    @patch("requests.post")
    def test_request_error(
        self, mock_post: MagicMock, mock_parse: MagicMock, data: Fixture
    ) -> None:
        """Should halt execution and return 'None' in case of a RequestError"""

        jwt, installation_id, url, headers, timeout = data

        mock_post.side_effect = RequestException
        mock_parse.return_value = None

        with raises(RequestException):
            result = get_access_token(jwt, installation_id)
            mock_post.assert_called_once_with(url, headers=headers, timeout=timeout)
            mock_parse.assert_not_called()
            assert result is None
