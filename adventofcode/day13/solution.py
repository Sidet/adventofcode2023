import os
from itertools import pairwise

from adventofcode import load, examples


def solve_1(inputs: list[str]) -> str:
    grids = extract_grids(inputs)

    total_row = 0
    total_col = 0

    for grid in grids:
        split_row = mirror_row(grid)
        split_col = 0
        if split_row == 0:
            transposed = transpose(grid)
            split_col = mirror_row(transposed)

        total_row += split_row
        total_col += split_col
    return str(total_row * 100 + total_col)


def solve_2(inputs: list[str]) -> str:
    grids = extract_grids(inputs)

    total_row = 0
    total_col = 0

    for grid in grids:
        split_row = mirror_row_smudge(grid)
        split_col = 0
        if split_row == 0:
            transposed = transpose(grid)
            split_col = mirror_row_smudge(transposed)

        total_row += split_row
        total_col += split_col
    return str(total_row * 100 + total_col)


def extract_grids(inputs):
    grids = []
    grid = []
    for line in inputs:
        if line:
            grid.append(line)
        else:
            grids.append(grid)
            grid = []

    if line:
        grids.append(grid)
    return grids


def mirror_row(grid: list[list[str]]) -> int:
    for r0_i, r1_i in pairwise(range(len(grid))):
        same = True
        while same and 0 <= r0_i and r1_i < len(grid):
            same = grid[r0_i] == grid[r1_i]
            r0_i -= 1
            r1_i += 1
        if same:
            return (r0_i + r1_i) // 2 + 1
    return 0


def mirror_row_smudge(grid: list[list[str]]) -> int:
    for r0_i, r1_i in pairwise(range(len(grid))):
        found = False
        same = True
        while same and 0 <= r0_i and r1_i < len(grid):
            same = grid[r0_i] == grid[r1_i]
            if not same and not found:
                found = True
                c = grid[r1_i]
                b = grid[r0_i]
                a = sum(a != b for a, b in zip(grid[r0_i], grid[r1_i]))
                same = sum(a != b for a, b in zip(grid[r0_i], grid[r1_i])) == 1
            r0_i -= 1
            r1_i += 1
        if same and found:
            return (r0_i + r1_i) // 2 + 1
    return 0


def transpose(grid: list[list[str]]) -> list[list[str]]:
    transposed = [[""] * len(grid) for _ in range(len(grid[0]))]
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            transposed[c][r] = cell
    return transposed


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check_1(directory, solve_1):
        result = solve_1(load.inputs(directory))
        print(f"Result for inputs: {result}")

    if examples.check_2(directory, solve_2):
        result = solve_2(load.inputs(directory))
        print(f"Result for inputs: {result}")
