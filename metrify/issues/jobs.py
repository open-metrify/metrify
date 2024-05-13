"""
FIXME: Arquivo ignorado por falta de STUBS para lib flask-apscheculer.
       -> Investigar possibilidade de gerar arquivos de stub
"""
# mypy: ignore-errors

from metrify import apscheduler


@apscheduler.task("interval", id="get_issue",
                  seconds=10, misfire_grace_time=900)
def get_issue() -> None:
    """..."""
    print("`get_issue` Job executed")
