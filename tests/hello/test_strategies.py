"""
Test suite for metrify.hello.strategies
"""

from metrify.hello.strategies import hello


def test_hello() -> None:
    """Should return 'Hello, World!'"""
    assert hello() == "Hello, World!"
