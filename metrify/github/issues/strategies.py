"""
Data collection strategies for GitHub issues.
"""

from gql import gql
from metrify import graphql


def get_issues() -> None:
    """Get all issues from a project."""

    query = gql("""
        query ($organization: String!) {
            organization(login: $organization) {
                projectsV2(first: 100) {
                    nodes {
                        id
                        title
                    }
                }
            }
        }
    """)

    # Variables to be passed to the query
    variables = {
        "organization": "open-metrify"
    }

    print(graphql.execute(query, variable_values=variables))  # type: ignore
