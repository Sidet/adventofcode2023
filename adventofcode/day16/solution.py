from __future__ import annotations
import os
from typing import Any

from adventofcode import load, examples


class Cell:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

    def __repr__(self) -> str:
        return f"<{Cell.__name__}({self.row}, {self.column})>"

    def __add__(self, other: Cell or tuple[int, int]):
        if isinstance(other, Cell):
            return Cell(self.row + other.row, self.column + other.column)
        else:
            return Cell(self.row + other[0], self.column + other[1])

    def __sub__(self, other: Cell):
        return Cell(self.row - other.row, self.column - other.column)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Cell):
            return self.row == other.row and self.column == other.column
        elif len(other) == 2:
            return self.row == other[0] and self.column == other[1]
        else:
            False

    def __hash__(self) -> int:
        return hash((self.row, self.column))

    def __lt__(self, other: Cell):
        return self.to_tuple() < other.to_tuple()

    def __gt__(self, other: Cell):
        return self.to_tuple() > other.to_tuple()

    def value(self, grid: list[list[str]]) -> str:
        return grid[self.row][self.column]

    def setvalue(self, value: Any, grid: list[list[str]]):
        if (
            0 <= self.row
            and self.row < len(grid)
            and 0 <= self.column
            and self.column < len(grid[0])
        ):
            grid[self.row][self.column] = value

    def to_tuple(self) -> tuple[int, int]:
        return self.row, self.column

    def inside(self, grid: list[list]) -> bool:
        return (
            0 <= self.row
            and self.row < len(grid)
            and 0 <= self.column
            and self.column < len(grid[0])
        )


def solve_1(inputs: list[str]) -> str:
    grid = []
    for line in inputs:
        grid.append(list(line))

    source = Cell(0, -1)
    start = Cell(0, 0)
    energized_grid = [[set() for _ in range(len(grid[0]))] for _ in range(len(grid))]
    trace_beam(source, start, grid, energized_grid)

    energized = sum(sum(len(c) > 0 for c in row) for row in energized_grid)
    return str(energized)


def solve_2(inputs: list[str]) -> str:
    grid = []
    for line in inputs:
        grid.append(list(line))

    rcd = []
    for c, direction in [(-1, (0, 1)), (len(grid[0]), (0, -1))]:
        for r in range(len(grid)):
            rcd.append((r, c, direction))
    for r, direction in [(-1, (1, 0)), (len(grid), (-1, 0))]:
        for c in range(len(grid[0])):
            rcd.append((r, c, direction))

    energies = []
    for r, c, direction in rcd:
        source = Cell(r, c)
        start = source + direction
        energized_grid = [
            [set() for _ in range(len(grid[0]))] for _ in range(len(grid))
        ]
        trace_beam(source, start, grid, energized_grid)
        energized = sum(sum(len(c) > 0 for c in row) for row in energized_grid)
        energies.append(energized)

    return str(max(energies))


def trace_beam(
    source: Cell, current: Cell, grid: list[list[str]], energized_grid: list[list[set]]
):
    while True:
        if not current.inside(grid):
            break

        direction = current - source
        energy_cell: set = energized_grid[current.row][current.column]
        d = direction.to_tuple()
        if d in energy_cell:
            break
        else:
            energy_cell.add(d)
        cell = current.value(grid)

        if cell == ".":
            source, current = current, current + direction
        elif cell == "/":
            if direction.row == 1:
                p = (0, -1)
            elif direction.row == -1:
                p = (0, 1)
            elif direction.column == 1:
                p = (-1, 0)
            else:
                p = (1, 0)
            source, current = current, current + p
        elif cell == "\\":
            if direction.row == 1:
                p = (0, 1)
            elif direction.row == -1:
                p = (0, -1)
            elif direction.column == 1:
                p = (1, 0)
            else:
                p = (-1, 0)
            source, current = current, current + p
        elif cell == "|":
            if direction.column == 0:
                source, current = current, current + direction
            else:
                p1 = (1, 0)
                p2 = (-1, 0)
                trace_beam(current, current + p1, grid, energized_grid)
                source, current = current, current + p2
        elif cell == "-":
            if direction.row == 0:
                source, current = current, current + direction
            else:
                p1 = (0, 1)
                p2 = (0, -1)
                trace_beam(current, current + p1, grid, energized_grid)
                source, current = current, current + p2


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check_1(directory, solve_1):
        result = solve_1(load.inputs(directory))
        print(f"Result for inputs: {result}")

    if examples.check_2(directory, solve_2):
        result = solve_2(load.inputs(directory))
        print(f"Result for inputs: {result}")
