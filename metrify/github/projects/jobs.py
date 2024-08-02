"""
metrify/projects/jobs.py
"""

from datetime import datetime, timedelta

from gql.transport.exceptions import TransportQueryError

from metrify import apscheduler, projects
from metrify.github.projects.strategies import get_projects


@apscheduler.task("interval", id="github.collect_projects", weeks=1,
                  misfire_grace_time=900, next_run_time=datetime.now() +
                  timedelta(seconds=10))  # TODO: Fix this
def collect_projects() -> None:
    """..."""

    try:
        result = get_projects()
    except TransportQueryError:
        return  # TODO: Handle this

    projects.clear()

    for repository in result["viewer"]["repositories"]["nodes"]:
        for project in repository["projectsV2"]["nodes"]:
            projects[project["number"]] = project["id"]
