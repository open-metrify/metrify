"""
Test suite for metrify.hello.strategies
"""

from metrify.hello.strategies import hello


class TestHello:
    """Test suite for `hello` function"""

    def test_hello(self) -> None:
        """Should return 'Hello, World!'"""
        assert hello() == "Hello, World!"
