from typing import Iterator

from aoc2023.utils import Solver


class PartOne(Solver):
    def _process_line(self, line: str, index: int) -> int | None:
        card, raw_numbers = line.split("|")
        raw_winning_numbers = card.split(":")[-1]

        def _parse_numbers(raw: str) -> Iterator[int]:
            yield from (int(x) for x in raw.split(" ") if x)

        winning_numbers = set(_parse_numbers(raw_winning_numbers))
        count = sum(
            1
            for number in _parse_numbers(raw_numbers)
            if number in winning_numbers
        )
        return 2 ** (count - 1) if count else 0
