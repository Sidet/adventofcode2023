import os

from adventofcode import load, examples


def solve_1(inputs: list[str]) -> str:
    grid: list[list[str]] = []
    for line in inputs:
        grid.append(list(line))

    grid = rotate_clockwise(grid)
    tilt_east(grid)
    load = load_on_west(grid)
    return str(load)


def solve_2(inputs: list[str]) -> str:
    grid: list[list[str]] = []
    for line in inputs:
        grid.append(list(line))
    loads = []
    for _ in range(1000000000):
        grid = rotate_clockwise(grid)
        loads.append(load_on_west(grid))
        c_length = find_cycle_length(loads)
        if c_length:
            break
        tilt_east(grid)
        grid = rotate_clockwise(grid)
        tilt_east(grid)
        grid = rotate_clockwise(grid)
        tilt_east(grid)
        grid = rotate_clockwise(grid)
        tilt_east(grid)
    cycles_loads = []
    for a in zip(range(len(loads))[-c_length:], loads[-c_length:]):
        cycles_loads.append(a)
    final_i = (1000000000 - cycles_loads[0][0]) % c_length
    return str(cycles_loads[final_i][1])


def rotate_clockwise(grid: list[list[str]]) -> list[list[str]]:
    transposed = [[""] * len(grid) for _ in range(len(grid[0]))]
    rt = len(grid) - 1
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            transposed[c][rt - r] = cell
    return transposed


def tilt_east(grid: list[list[str]]):
    for r, row in enumerate(grid):
        tilted_row = ""
        rocks = 0
        for c, cell in enumerate(row):
            if cell == "O":
                rocks += 1
            elif cell == "#":
                tilted_row += tilted_fragment(tilted_row, rocks, c)
                rocks = 0

        if len(tilted_row) < len(row):
            tilted_row += tilted_fragment(tilted_row, rocks, c + 1)[:-1]
        grid[r] = list(tilted_row)


def tilted_fragment(tilted_row: list[str], rocks: int, cell: int) -> str:
    last = len(tilted_row)
    return "." * (cell - last - rocks) + "O" * rocks + "#"


def load_on_west(grid: list[list[str]]):
    total = 0
    for row in grid:
        for c, cell in enumerate(row, 1):
            if cell == "O":
                total += c
    return total


def find_cycle_length(loads: list[int]) -> bool:
    for i in range(1, (len(loads) // 5) + 2):
        test_cycle = loads[-i:]
        cycle_length = len(test_cycle)
        cycles_5 = loads[-cycle_length * 5 :]
        if cycles_5 == test_cycle * 5:
            return cycle_length
    return 0


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check_1(directory, solve_1):
        result = solve_1(load.inputs(directory))
        print(f"Result for inputs: {result}")

    if examples.check_2(directory, solve_2):
        result = solve_2(load.inputs(directory))
        print(f"Result for inputs: {result}")
