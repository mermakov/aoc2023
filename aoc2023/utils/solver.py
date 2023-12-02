from abc import ABC, abstractmethod
from pathlib import Path


class Solver(ABC):
    _STRIP: bool = True

    def __init__(self) -> None:
        self._accumulator = 0

    def __init_subclass__(cls, strip: bool = True) -> None:
        cls._STRIP = strip

    @abstractmethod
    def _process_line(self, line: str) -> int | None:
        pass

    def postprocess(self) -> None:
        pass

    def __call__(self, path: Path) -> int:
        with path.open() as f:
            for line in f.readlines():
                value = self._process_line(
                    line.strip() if self._STRIP else line
                )
                if value is not None:
                    self._accumulator += value

        self.postprocess()
        return self._accumulator
