import os

from adventofcode import load, examples

name_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solve(inputs: list[str]) -> str:
    total = 0
    for line in inputs:
        total += int(first_digit(line) + last_digit(line))
    return str(total)


def first_digit(line: str) -> str:
    while line:
        if line[0].isdigit():
            return line[0]
        for name, digit in name_to_digit.items():
            if line.startswith(name):
                return digit
        line = line[1:]


def last_digit(full_line: str) -> str:
    line = ""
    for char in reversed(full_line):
        line = char + line
        if char.isdigit():
            return char
        for name, digit in name_to_digit.items():
            if line.startswith(name):
                return digit


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check(directory, solve):
        result = solve(load.inputs(directory))
        print(f"Result for inputs: {result}")
