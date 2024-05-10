"""
...
"""

from metrify import apscheduler


@apscheduler.task('interval', id='hello_job', seconds=10, misfire_grace_time=900)
def get_issue():
    """
    ...
    """
    print('Job 1 executed')
