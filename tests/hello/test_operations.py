from metrify.hello.operations import hello


def test_hello():
    """Returns 'Hello, World!'"""
    assert hello() == "Hello, World!"
