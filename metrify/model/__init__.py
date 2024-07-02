"""
metrify/model/__init__.py

Exports entity model classes for the application
"""


from typing import TypedDict


class Developer(TypedDict):
    """
    Developer class

    :ivar name: Name attribute for the developer object
    :vartype name: str
    """

    name: str


class Issue(TypedDict):
    """
    Issue class

    :ivar code: Code attribute for the issue object
    :vartype code: str
    """

    code: str


__all__ = ["Developer", "Issue"]
