from collections.abc import Callable
from datetime import datetime
from typing import Never

from flask import Flask

class _Undefined(object): ...
class BaseTrigger(object): ...

class APScheduler(object):
    def task(
        self,
        trigger: str | BaseTrigger,
        args: list[object] | tuple[object] | None = None,
        kwargs: dict[object, object] | None = None,
        id: str | None = None,
        name: str | None = None,
        misfire_grace_time: _Undefined | int = _Undefined(),
        coalesce: bool | _Undefined = _Undefined(),
        max_instances: int | _Undefined = _Undefined(),
        next_run_time: datetime | _Undefined = _Undefined(),
        jobstore: str = "default",
        executor: str = "default",
        **trigger_args: dict[str, object | int] | int,
    ) -> Callable[[object], object] | Never: ...
    def init_app(self, app: Flask) -> None: ...
    def start(self, paused: bool = False) -> None: ...
