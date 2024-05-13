from typing import Any, TypedDict, Unpack
from flask import Flask, Response

class Kwargs(TypedDict, total=False): ...

class PyMongo(object):
    def __init__(  # type: ignore[misc] # noqa: F821
        self,
        app: Flask | None = None,
        uri: str | None = None,
        *args: tuple[Any],
        **kwargs: dict[Any, Any]
    ) -> None: ...
    def init_app(self, app, uri=None, *args, **kwargs) -> None: ...
    def send_file(
        self,
        filename: str,
        base: str = "fs",
        version: bool = -1,
        cache_for: int = 31536000,
    ) -> Response:
        def save_file(self, filename: str, fileobj: Any, base: str = "fs", content_type: str = None, **kwargs: Unpack[Kwargs]) -> Any:  # type: ignore[misc] # noqa: F821
            ...
