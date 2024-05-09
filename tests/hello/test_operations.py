"""
Test suite for metrify.hello.operations
"""

from metrify.hello.operations import hello


def test_hello() -> None:
    """Returns 'Hello, World!'"""
    assert hello() == "Hello, World!"
