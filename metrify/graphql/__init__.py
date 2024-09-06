"""
metrify/graphql/__init__.py

Exports utility functions for working with GraphQL
"""
import os

type QueryDict = dict[str, str]
"""
In-memory representation of the GraphQL queries compiled from `gql` files.
The key-value pairs are assembled using the original filenames as keys (file extensions are stripped), and the contents as values.
"""


def load_queries() -> QueryDict:
    """
    Load `gql` query files to memory.

    :return: The object containing the queries
    :rtype: :class:`QueryDict`
    """

    query_dir = f'{os.getcwd()}/metrify/graphql/queries'

    return {
        os.path.splitext(filename)[0]: open(os.path.join(query_dir, filename), 'r').read()
        for filename in os.listdir(query_dir)
        if os.path.isfile(os.path.join(query_dir, filename))
    }


__all__ = ["load_queries"]
