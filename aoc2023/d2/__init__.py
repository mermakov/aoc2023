import re
from collections import defaultdict

from aoc2023.utils import Solver

_COLOR_LIMITS = {"red": 12, "green": 13, "blue": 14}

_COUNT_PTN = re.compile(
    rf"(?P<count>\d+) (?P<color>{'|'.join(_COLOR_LIMITS)})"
)


class PartOne(Solver):
    _game_pattern: re.Pattern

    def __init__(self) -> None:
        super().__init__()

    def _get_dice_counts(self, line: str) -> tuple[int, dict[str, list[int]]]:
        game_info, rolls = line.split(":")
        game_id = int(game_info.split(" ")[-1])

        dice_counts = defaultdict(list)

        for roll in rolls.split(";"):
            for count, color in _COUNT_PTN.findall(roll):
                dice_counts[color].append(int(count))

        return game_id, dice_counts

    def _process_line(self, line: str, index: int) -> int | None:
        game_id, dice_counts = self._get_dice_counts(line)
        for color, counts in dice_counts.items():
            if any(count > _COLOR_LIMITS[color] for count in counts):
                return 0

        return game_id


class PartTwo(PartOne):
    def _process_line(self, line: str, index: int) -> int | None:
        _, dice_counts = self._get_dice_counts(line)
        power = 1
        for color in _COLOR_LIMITS:
            counts = dice_counts.get(color)
            if counts:
                power *= max(counts)
        return power
