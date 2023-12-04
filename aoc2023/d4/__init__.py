from collections import defaultdict
from typing import Iterator

from aoc2023.utils import Solver


class PartOne(Solver):
    @staticmethod
    def _parse_line(line: str) -> int:
        card, raw_numbers = line.split("|")
        raw_winning_numbers = card.split(":")[-1]

        def _parse_numbers(raw: str) -> Iterator[int]:
            yield from (int(x) for x in raw.split(" ") if x)

        winning_numbers = set(_parse_numbers(raw_winning_numbers))

        return sum(
            1
            for number in _parse_numbers(raw_numbers)
            if number in winning_numbers
        )

    def _process_line(self, line: str, index: int) -> int | None:
        count = self._parse_line(line)
        return 2 ** (count - 1) if count else 0


class PartTwo(PartOne):
    _scratchcards: dict[int, int]

    def __init__(self) -> None:
        super().__init__()
        self._scratchcards = defaultdict(int)

    def _process_line(self, line: str, index: int) -> int | None:
        self._scratchcards[index] += 1
        for i in range(self._parse_line(line)):
            self._scratchcards[index + i + 1] += self._scratchcards[index]
        return None

    def postprocess(self) -> None:
        self._accumulator += sum(self._scratchcards.values())
