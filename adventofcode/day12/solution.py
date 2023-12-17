import os
import math
import functools

from adventofcode import load, examples


def solve_1(inputs: list[str]) -> str:
    total = 0
    for line in inputs:
        springs, groups_str = line.split(" ")
        groups = [int(n) for n in groups_str.split(",")]
        permutations = count_permutations(springs, tuple(groups))
        total += permutations
    return str(total)


def solve_2(inputs: list[str]) -> str:
    total = 0
    for line in inputs:
        springs, groups_str = line.split(" ")
        groups = [int(n) for n in groups_str.split(",")]
        springs = unfold_springs(springs)
        groups = unfold_groups(groups)
        permutations = count_permutations(springs, tuple(groups))
        total += permutations
    return str(total)


@functools.cache
def count_permutations(line: str, groups: tuple) -> int:
    groups = groups[:]
    symbols = set(line)
    if len(symbols) == 1 and "?" in symbols:
        return count_clean_permutations(len(line), groups)
    if len(groups) == 0:
        if len(line) == 0 or "#" not in symbols:
            return 1
        else:
            return 0

    group_len = groups[0]
    groups = tuple(groups[1:])
    min_len = min_length(groups)
    if min_len == 0:
        place_in = line + "."
    else:
        place_in = line[:-min_len]

    if len(place_in) - 1 < group_len:
        return 0
    total = 0
    for start in range(len(place_in) - group_len):
        end = start + group_len
        potential = "." * start + "#" * group_len + "."
        if valid_arrangement(place_in[: end + 1], potential):
            total += count_permutations(line[end + 1 :], groups)
    return total


def min_length(groups: list[int]) -> int:
    if len(groups) < 2:
        gaps = 0
    else:
        gaps = len(groups) - 1
    return sum(groups) + gaps


def count_clean_permutations(length: str, groups: list[int]) -> int:
    # balls and bins combinatorics problem solution
    min_len = min_length(groups)
    balls = length - min_len
    bins = len(groups) + 1
    return int(
        math.factorial(balls + bins - 1)
        / math.factorial(balls)
        / math.factorial(bins - 1)
    )


def valid_arrangement(line: str, arrangement: str) -> bool:
    return all(a == "?" or a == b for a, b in zip(line, arrangement))


def unfold_springs(springs: str) -> str:
    return "?".join([springs] * 5)


def unfold_groups(groups: list[int]) -> list[int]:
    return [g for _ in range(5) for g in groups]


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check_1(directory, solve_1):
        result = solve_1(load.inputs(directory))
        print(f"Result for inputs: {result}")

    if examples.check_2(directory, solve_2):
        result = solve_2(load.inputs(directory))
        print(f"Result for inputs: {result}")
