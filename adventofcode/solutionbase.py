import os

from adventofcode import load, examples


def solve(inputs: list[str]) -> str:
    pass


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check(directory, solve):
        result = solve(load.inputs(directory))
        print(f"Result for inputs: {result}")
