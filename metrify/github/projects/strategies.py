"""
Data collection strategies for GitHub Projects.
"""

from typing import Any
from gql import gql
from metrify import graphql, queries


def get_projects() -> dict[str, dict[Any, Any]]:
    """Get all projects from every repository"""

    query = gql(queries["ProjectsQuery"])

    return graphql.execute(query)
