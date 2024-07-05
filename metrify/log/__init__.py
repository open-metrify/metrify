"""
metrify/log/__init__.py

Contains logging configuration and util function implementations.
"""

import json
import datetime
from logging import Formatter, Filter, LogRecord, INFO
from typing import override

LOG_RECORD_BUILTIN_ATTRS = {
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "message",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
    "taskName",
}


class JSONFormatter(Formatter):
    """
    Custom JSON log formatter implementation for producing JSONL log files.
    """

    def __init__(self, *, fmt_keys: dict[str, str] | None = None) -> None:
        super().__init__()
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    @override
    def format(self, record: LogRecord) -> str:
        return json.dumps(self._transform(record), default=str)

    def _transform(self, record: LogRecord) -> dict[str, str]:
        record_fields = {
            "message": record.getMessage(),
            "timestamp": datetime.datetime.fromtimestamp(
                record.created, tz=datetime.timezone.utc
            ).isoformat(),
        }

        if record.exc_info is not None:
            record_fields["exc_info"] = self.formatException(record.exc_info)

        if record.stack_info is not None:
            record_fields["stack_info"] = self.formatStack(record.stack_info)

        message = {
            key: msg_val
            if (msg_val := record_fields.pop(val, None)) is not None
            else getattr(record, val)
            for key, val in self.fmt_keys.items()
        }
        message.update(record_fields)

        for key, val in record.__dict__.items():
            if key not in LOG_RECORD_BUILTIN_ATTRS:
                message[key] = val

        return message


class NonErrorFilter(Filter):
    """
    Custom log filter implementation for separating error messages from
    info/debug messages.
    """
    @override
    def filter(self, record: LogRecord) -> bool | LogRecord:
        return record.levelno <= INFO


__all__ = ["JSONFormatter", "NonErrorFilter"]
