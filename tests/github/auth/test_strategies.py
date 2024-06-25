"""
Test suite for metrify.github.auth.strategies
"""

from typing import Generator
from unittest.mock import MagicMock, patch
from pytest import raises
import pytest

from requests import RequestException

from metrify.github.auth.strategies import get_access_token


class TestGetAccessToken:
    """Test suite for `get_access_token` function"""

    @pytest.fixture(scope="class")
    def data(self) -> Generator[tuple, None, None]:
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

    @patch("metrify.github.auth.strategies.json")
    @patch("requests.post")
    def test_returns_token(
            self,
            mock_post: MagicMock,
            mock_json: MagicMock,
            data: tuple):
        """
        Should correctly extract and return the 'token' attribute value from
        the response body
        """

        jwt, installation_id, url, headers, timeout = data

        token_value = "test_token"
        response_content = "{ token: { " + token_value + " } }"

        mock_json.loads = MagicMock()
        mock_json.loads.return_value = {"token": token_value}
        response = MagicMock()
        response.content = response_content
        mock_post.return_value = response

        result = get_access_token(jwt, installation_id)

        mock_post.assert_called_once_with(
            url, headers=headers, timeout=timeout)
        mock_json.loads.assert_called_once_with(response_content)
        assert result == token_value

    @patch("metrify.github.auth.strategies.json")
    @patch("requests.post")
    def test_request_error(
            self,
            mock_post: MagicMock,
            mock_json: MagicMock,
            data: tuple):
        """Should halt execution and return 'None' in case of a RequestError"""

        jwt, installation_id, url, headers, timeout = data

        mock_post.side_effect = RequestException

        with raises(RequestException):
            result = get_access_token(jwt, installation_id)
            mock_post.assert_called_once_with(
                url, headers=headers, timeout=timeout)
            mock_json.assert_not_called()
            assert result is None
