import os
from collections import defaultdict

from adventofcode import load, examples


NOT_SYMBOLS = set([".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])


def solve_1(inputs: list[str]) -> str:
    grid: list[list[str]] = []
    for line in inputs:
        grid.append(list(line))

    numbers_starts: list[tuple[int, int]] = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c].isdigit() and (c == 0 or not grid[r][c - 1].isdigit()):
                numbers_starts.append((r, c))

    total = 0
    for row, col in numbers_starts:
        number = get_number(row, col, grid)
        if is_part_number(row, col, len(number), grid):
            total += int("".join(number))
    return str(total)


def get_number(row_number: int, col: int, grid: list[list[str]]) -> str:
    row: list[str] = grid[row_number]
    digits = []
    for char in row[col:]:
        if char.isdigit():
            digits.append(char)
        else:
            break
    return digits


def is_part_number(row: int, col: int, number_len: int, grid: list[list[str]]) -> bool:
    potentials: set[str] = set()

    rows = [r for r in range(row - 1, row + 2) if 0 <= r and r < len(grid)]
    columns = [
        c for c in range(col - 1, col + number_len + 1) if 0 <= c and c < len(grid[0])
    ]

    for row_i in rows:
        for col_i in columns:
            potentials.add(grid[row_i][col_i])

    symbols = potentials - NOT_SYMBOLS
    return len(symbols) > 0


def solve(inputs: list[str]) -> str:
    grid: list[list[str]] = []
    for line in inputs:
        grid.append(list(line))

    numbers_starts: list[tuple[int, int]] = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c].isdigit() and (c == 0 or not grid[r][c - 1].isdigit()):
                numbers_starts.append((r, c))

    total = 0
    gears: dict[tuple(int, int), list[int]] = defaultdict(list)
    for row, col in numbers_starts:
        number = get_number(row, col, grid)
        gears_locations = part_of_gear(row, col, len(number), grid)
        for r, c in gears_locations:
            gears[(r, c)].append(int("".join(number)))

    total = 0
    for _, numbers in gears.items():
        if len(numbers) == 2:
            total += numbers[0] * numbers[1]
    return str(total)


def part_of_gear(
    row: int, col: int, number_len: int, grid: list[list[str]]
) -> list[tuple[int, int]]:
    cells: list[tuple[int, int]] = []
    columns = [
        c for c in range(col - 1, col + number_len + 1) if 0 <= c and c < len(grid[0])
    ]
    if 0 <= row - 1:
        for c in columns:
            cells.append((row - 1, c))
    if row + 1 < len(grid):
        for c in columns:
            cells.append((row + 1, c))
    if 0 <= col - 1:
        cells.append((row, col - 1))
    if col + number_len + 1 < len(grid[0]):
        cells.append((row, col + number_len))

    gears: list[tuple[int, int]] = []
    for r, c in cells:
        if grid[r][c] == "*":
            gears.append((r, c))
    return gears


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check(directory, solve):
        result = solve(load.inputs(directory))
        print(f"Result for inputs: {result}")
