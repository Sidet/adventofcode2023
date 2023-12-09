import os

from adventofcode import load, examples


def solve_1(inputs: list[str]) -> str:
    pass


def solve_2(inputs: list[str]) -> str:
    pass


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check_1(directory, solve_1):
        result = solve_1(load.inputs(directory))
        print(f"Result for inputs: {result}")

    if examples.check_2(directory, solve_2):
        result = solve_2(load.inputs(directory))
        print(f"Result for inputs: {result}")
