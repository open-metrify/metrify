"""
metrify/issues/jobs.py
"""

from metrify import apscheduler
from metrify.github.issues.strategies import get_issues


@apscheduler.task("interval", id="github.collect_data",
                  seconds=5, misfire_grace_time=900)
def collect_data() -> None:
    """..."""

    get_issues()
