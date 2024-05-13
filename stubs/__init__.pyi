from collections.abc import Callable
from typing import Protocol

class APScheduler(Protocol):
    @property
    def task(self) -> Callable:
        """Get the base scheduler decorator"""
        ...
