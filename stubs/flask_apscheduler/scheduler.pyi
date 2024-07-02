from datetime import datetime, tzinfo
from typing import Any, Callable, List, Never, Type, TypedDict
from typing_extensions import Unpack

from flask import Flask

type Args = list[Any] | tuple[Any] | None  # type: ignore[misc, valid-type] # noqa: F821
type Kwargs = dict[Any, Any] | None  # type: ignore[misc, valid-type] # noqa: F821
type F = Callable[[Any], Any] | Never  # type: ignore[misc, valid-type] # noqa: F821

class _Undefined(object): ...
class BaseTrigger(object): ...

class TriggerArgs(TypedDict, total=False):
    weeks: int
    days: int
    hours: int
    minutes: int
    seconds: int
    start_date: datetime | str
    end_date: datetime | str
    timezone: Type[tzinfo] | str
    jitter: int | None

class APScheduler(object):
    def task(
        self,
        trigger: str | BaseTrigger,
        args: Args = None,
        kwargs: Kwargs = None,
        id: str | None = None,
        name: str | None = None,
        misfire_grace_time: _Undefined | int = _Undefined(),
        coalesce: bool | _Undefined = _Undefined(),
        max_instances: int | _Undefined = _Undefined(),
        next_run_time: datetime | _Undefined = _Undefined(),
        jobstore: str = "default",
        executor: str = "default",
        **trigger_args: Unpack[TriggerArgs],
    ) -> F: ...
    def init_app(self, app: Flask) -> None: ...
    def start(self, paused: bool = False) -> None: ...

    allowed_hosts: List[str] = ["*"]
    auth: dict[str, str] | None = None
    api_enabled: bool = False
    api_prefix: str = "/scheduler"
    endpoint_prefix: str = "scheduler."
    app: Flask | None = None
