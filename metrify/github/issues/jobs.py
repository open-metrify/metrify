"""
metrify/issues/jobs.py
"""

from metrify import apscheduler


@apscheduler.task("interval", id="github.get_issue",
                  seconds=10, misfire_grace_time=900)
def get_issue() -> None:
    """..."""
    print("`get_issue` Job executed")
