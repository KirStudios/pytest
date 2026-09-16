from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Annotated

from kirtest.core.config.config import TESTS

if TYPE_CHECKING:
    from types import FunctionType


@dataclass
class Test:
    function: FunctionType

    @property
    def name(self) -> str:
        return self.function.__name__


@dataclass
class FileContent:
    path: Path
    tests: list[Test]


class Discovery:
    def __init__(
        self,
        path: Annotated[
            Path | None,
            "Directory containing the test files to discover.",
        ] = None,
    ):
        self.path = self._sanitize(path)

    def _sanitize(self, path: Path | None) -> Path:
        if path is None:
            return Path.cwd() / TESTS

        return path.resolve()
