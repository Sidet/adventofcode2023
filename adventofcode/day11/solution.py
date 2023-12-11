import os

from adventofcode import load, examples


def solve_1(inputs: list[str]) -> str:
    return solve(inputs, 2)


def solve_2ex(inputs: list[str]) -> str:
    return solve(inputs, 10)


def solve_2(inputs: list[str]) -> str:
    return solve(inputs, 1000000)


def solve(inputs: list[str], expansion_rate: int) -> str:
    expansion_rate -= 1
    observation: list[list[str]] = []
    for line in inputs:
        observation.append(list(line))

    empty_rows = []
    for r, row in enumerate(observation):
        if all("." == cell for cell in row):
            empty_rows.append(r)

    column_is_empty = [True] * len(observation[0])
    for row in observation:
        for c, cell in enumerate(row):
            column_is_empty[c] &= "." == cell

    empty_columns = [c for c, is_empty in enumerate(column_is_empty) if is_empty]

    galaxies = []
    for r, row in enumerate(observation):
        for c, cell in enumerate(row):
            if cell == "#":
                galaxies.append((r, c))

    total = 0
    for g0, gal0 in enumerate(galaxies):
        for gal1 in galaxies[g0 + 1 :]:
            r = count_numbers_between(gal0[0], gal1[0], empty_rows)
            c = count_numbers_between(gal0[1], gal1[1], empty_columns)
            distance = (
                abs(gal0[0] - gal1[0])
                + r * expansion_rate
                + abs(gal0[1] - gal1[1])
                + c * expansion_rate
            )
            total += distance
    return str(total)


def count_numbers_between(a: int, b: int, numbers: list[int]) -> int:
    if a > b:
        a, b = b, a
    found = False
    for i_start, n in enumerate(numbers):
        if a < n:
            found = True
            break
    if not found:
        i_start = len(numbers)
    found = False
    for i_end, n in enumerate(numbers[i_start:], i_start):
        if b < n:
            found = True
            break
    if not found:
        i_end = len(numbers)
    return i_end - i_start


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check_1(directory, solve_1):
        result = solve_1(load.inputs(directory))
        print(f"Result for inputs: {result}")

    if examples.check_2(directory, solve_2ex):
        result = solve_2(load.inputs(directory))
        print(f"Result for inputs: {result}")
