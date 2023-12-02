import argparse
import importlib
import sys
from pathlib import Path


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--part", choices=(1, 2), type=int, default=1)
    parser.add_argument("--test", action="store_true")
    parser.add_argument("-i", "--input", type=Path)
    parser.add_argument("day")

    return parser.parse_args()


def main():
    opts = _parse_args()
    solver_name = f"Part{'One' if opts.part == 1 else 'Two'}"

    try:
        module = importlib.import_module(f"aoc2023.d{opts.day}")
        solver = getattr(module, solver_name)
    except ModuleNotFoundError:
        print(f"No day '{opts.day}' found!", file=sys.stderr)
        return 1
    except AttributeError:
        print(
            f"Day '{opts.day}' does not define '{solver_name}'",
            file=sys.stderr,
        )
        return 1

    input_ = opts.input or (
        Path(module.__file__).parent
        / ("test.txt" if opts.test else "input.txt")
    )
    print(solver()(input_))


if __name__ == "__main__":
    sys.exit(main())
