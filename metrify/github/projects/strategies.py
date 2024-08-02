"""
Data collection strategies for GitHub Projects.
"""

from gql import gql
from metrify import graphql


def get_projects() -> dict[str, dict]:
    """Get all projects from every repository"""

    query = gql("""
        query {
            viewer {
                repositories(first: 100) {
                    nodes {
                        projectsV2(first: 100) {
                            nodes {
                                number
                                id
                            }
                        }
                    }
                }
            }
        }
    """)

    return graphql.execute(query)  # pylint: disable=attr-defined
