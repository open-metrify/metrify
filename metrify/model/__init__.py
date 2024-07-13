"""
metrify/model/__init__.py

Exports entity model classes for the application
"""


from typing import TypedDict


class TeamMember(TypedDict):
    """
    TeamMember class

    :ivar name: Name attribute for the team member object
    :vartype name: str
    """

    name: str


class HistoryStatus(TypedDict):
    """
    HistoryStatus class

    :ivar status: Status attribute for the history status object
    :vartype status: str
    """

    status: str
    timestamp: int


class Issue(TypedDict):
    """
    Issue class

    :ivar number: Number attribute for the issue object
    :vartype number: int
    """

    number: int
    points: int
    developer: TeamMember
    tester: TeamMember
    history: list[HistoryStatus]


__all__ = ["TeamMember", "HistoryStatus", "Issue"]
