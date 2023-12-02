import re

from aoc2023.utils import Solver

_COLOR_LIMITS = {"red": 12, "green": 13, "blue": 14}

_COUNT_PTN = re.compile(rf"(?P<count>\d+) (?P<color>{'|'.join(_COLOR_LIMITS)})")


class PartOne(Solver):
    _game_pattern: re.Pattern

    def __init__(self) -> None:
        super().__init__()

    def _process_line(self, line: str) -> int | None:
        game_info, rolls = line.split(":")
        game_id = int(game_info.split(" ")[-1])

        for roll in rolls.split(";"):
            dice_counts = _COUNT_PTN.findall(roll)
            if any(
                int(count) > _COLOR_LIMITS[color]
                for count, color in dice_counts
            ):
                return 0

        return game_id
