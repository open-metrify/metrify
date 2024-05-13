"""
Test suite for metrify.hello.strategies
"""

from metrify.hello.strategies import hello


def test_hello() -> None:
    """Returns 'Hello, World!'"""
    assert hello() == "Hello, World!"
