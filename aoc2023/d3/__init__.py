from collections import defaultdict

from aoc2023.utils import Solver
from aoc2023.utils.types import Coordinate


class PartOne(Solver):
    _numbers: dict[Coordinate, list[int]]
    _symbols: dict[Coordinate, str]

    def __init__(self) -> None:
        super().__init__()
        self._numbers = {}
        self._symbols = {}

    def _process_line(self, line: str, index: int) -> int | None:
        current_number = None
        current_number_start = None

        def _record_number():
            nonlocal current_number
            nonlocal current_number_start

            if current_number_start is not None:
                self._numbers[(index, current_number_start)] = current_number
                current_number = None
                current_number_start = None

        for j, char in enumerate(line):
            if "0" <= char <= "9":
                if current_number_start is None:
                    current_number_start = j
                    current_number = [int(char)]
                else:
                    current_number.append(int(char))
            else:
                _record_number()
                if char != ".":
                    self._symbols[(index, j)] = char

        _record_number()

        return None

    def _get_adjacent_symbols(
        self, coord: Coordinate, length: int
    ) -> dict[Coordinate, str]:
        y, x = coord
        result = {}

        for i in (-1, 0, 1):
            for j in range(-1, length + 1):
                char = self._symbols.get((y + i, x + j))
                if char is not None:
                    result[(y + i, x + j)] = char

        return result

    @staticmethod
    def _get_number_value(number: list[int]) -> int:
        result = 0
        power = 1

        for digit in reversed(number):
            result += power * digit
            power *= 10

        return result

    def postprocess(self) -> None:
        for coord, number in self._numbers.items():
            if self._get_adjacent_symbols(coord, len(number)):
                self._accumulator += self._get_number_value(number)


class PartTwo(PartOne):
    def postprocess(self) -> None:
        gears: dict[Coordinate, list] = defaultdict(list)
        for coord, number in self._numbers.items():
            for symbol_coord, symbol in self._get_adjacent_symbols(
                coord, len(number)
            ).items():
                if symbol == "*":
                    gears[symbol_coord].append(number)

        for gear_numbers in gears.values():
            if len(gear_numbers) == 2:
                self._accumulator += self._get_number_value(
                    gear_numbers[0]
                ) * self._get_number_value(gear_numbers[1])
