from typing import Any
from flask import Flask, Response

type Kwargs = Any  # type: ignore[misc, valid-type] # noqa: F821
type Args = Any  # type: ignore[misc, valid-type] # noqa: F821
type File = Any  # type: ignore[misc, valid-type] # noqa: F821
type Id = Any  # type: ignore[misc, valid-type] # noqa: F821

class PyMongo(object):
    def __init__(
        self,
        app: Flask | None = None,
        uri: str | None = None,
        *args: Args,
        **kwargs: Kwargs,
    ) -> None: ...
    def init_app(
        self,
        app: Flask,
        uri: str | None = None,
        *args: Args,
        **kwargs: Kwargs,
    ) -> None: ...
    def send_file(
        self,
        filename: str,
        base: str = "fs",
        version: bool | int = -1,
        cache_for: int = 31536000,
    ) -> Response: ...
    def save_file(
        self,
        filename: str,
        fileobj: File,
        base: str = "fs",
        content_type: str | None = None,
        **kwargs: Kwargs,
    ) -> Id: ...
