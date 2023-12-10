from __future__ import annotations
import os
from typing import Iterator

from adventofcode import load, examples

START = "S"


class Index:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

    def __repr__(self) -> str:
        return f"<{Index.__name__}({self.row}, {self.column})>"

    def __add__(self, other: Index or tuple[int, int]):
        if isinstance(other, Index):
            return Index(self.row + other.row, self.column + other.column)
        else:
            return Index(self.row + other[0], self.column + other[1])

    def __sub__(self, other: Index):
        return Index(self.row - other.row, self.column - other.column)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Index):
            return self.row == other.row and self.column == other.column
        elif len(other) == 2:
            return self.row == other[0] and self.column == other[1]
        else:
            False

    def __hash__(self) -> int:
        return hash((self.row, self.column))

    def __lt__(self, other: Index):
        return self.to_tuple() < other.to_tuple()

    def __gt__(self, other: Index):
        return self.to_tuple() > other.to_tuple()

    def value(self, grid: list[list[str]]) -> str:
        return grid[self.row][self.column]

    def setvalue(self, value: str, grid: list[list[str]]):
        if (
            0 <= self.row
            and self.row < len(grid)
            and 0 <= self.column
            and self.column < len(grid[0])
        ):
            grid[self.row][self.column] = value

    def to_tuple(self) -> tuple[int, int]:
        return self.row, self.column


def solve_1(inputs: list[str]) -> str:
    grid = to_grid(inputs)
    start = start_index(grid)
    exit = list(exits_from_start(start, grid))[0]
    pipes = full_pipe(start, exit, grid)
    return str(len(pipes) // 2)


def full_pipe(start: Index, exit: Index, grid: list[list[str]]) -> list[Index]:
    previous = start
    pipes: list[Index] = []
    pipes.append(start)
    while exit != start:
        pipes.append(exit)
        pipe = exit.value(grid)
        exit, previous = next_pipe(previous, exit, pipe), exit
    return pipes


def replace_start_with_pipe(grid, start, exits):
    for shape, exit_deltas in PIPES_EXITS.items():
        deltas = [e - start for e in exits]
        if all(d in exit_deltas for d in deltas):
            start.setvalue(shape, grid)
            break


def solve_2(inputs: list[str]) -> str:
    grid = to_grid(inputs)

    start = start_index(grid)
    exits = list(exits_from_start(start, grid))
    replace_start_with_pipe(grid, start, exits)

    pipes = full_pipe(start, exits[0], grid)

    encs = enclosed(pipes, grid)
    return str(len(encs))


def to_grid(lines: list[str]) -> list[list[str]]:
    return [[c for c in line] for line in lines]


def start_index(grid: list[list[str]]) -> Index:
    for r, row in enumerate(grid):
        if START in row:
            return Index(r, row.index(START))


ADJECENT: list[tuple[int, int]] = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def adjecents(index: Index) -> Iterator[Index]:
    for adj in ADJECENT:
        yield index + adj


def exits_from_start(start: Index, grid: list[list[str]]) -> Iterator[Index]:
    for cell in adjecents(start):
        pipe = cell.value(grid)
        potentials = pipe_exits(cell, pipe)
        for exit in potentials:
            if exit == start:
                yield cell


def next_pipe(previous: Index, current: Index, pipe: str) -> Index:
    exit0, exit1 = pipe_exits(current, pipe)
    if exit0 == previous:
        return exit1
    else:
        return exit0


PIPES_EXITS = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "F": ((1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((0, -1), (1, 0)),
    "L": ((-1, 0), (0, 1)),
}

PIPES_WALLS = {
    "-": ((-1, 0), (1, 0)),
    "|": ((0, -1), (0, 1)),
    "J": ((1, 0), (0, 1)),
    "F": ((-1, 0), (0, -1)),
    "L": ((0, -1), (1, 0)),
    "7": ((-1, 0), (0, 1)),
}


def pipe_exits(index: Index, pipe: str) -> tuple[Index, Index] or tuple:
    if pipe in PIPES_EXITS:
        a, b = PIPES_EXITS[pipe]
        return index + a, index + b
    else:
        return ()


def pipe_walls(index: Index, pipe: str) -> tuple[Index, Index] or tuple:
    if pipe in PIPES_WALLS:
        a, b = PIPES_WALLS[pipe]
        return index + a, index + b
    else:
        return ()


def enclosed(pipes: list[Index], grid: list[list[int]]) -> set[Index]:
    edge_index: Index = sorted(pipes)[0]
    i = pipes.index(edge_index)
    pipes = pipes[i:] + pipes[:i]
    pipe = edge_index.value(grid)
    outside = pipe_walls(edge_index, pipe)
    inside = ()
    interface: list[tuple[Index, list[Index], list[Index]]] = [
        (edge_index, outside, inside)
    ]
    for i, interface_index in enumerate(pipes[1:]):
        pipe = interface_index.value(grid)
        if pipe in ["|", "-"]:
            one_side, other_side = pipe_walls(interface_index, pipe)
            one_side = [one_side]
            other_side = [other_side]
        else:
            one_side = pipe_walls(interface_index, pipe)
            other_side = []
        interface.append(
            analyze_interface(interface[-1], interface_index, one_side, other_side)
        )

    return analyze_inside(pipes, [inside for _, _, inside in interface])


def analyze_interface(
    comps: tuple[Index, list[Index], list[Index]],
    current_i: Index,
    one_side: list[Index],
    other_side: list[Index],
) -> tuple[Index, list[Index], list[Index]]:
    last_index, last_outside, last_inside = comps
    delta_i = last_index - current_i
    one_inside = current_i, other_side, one_side
    other_inside = current_i, one_side, other_side
    if last_inside:
        if one_side:
            if any(side_i + delta_i in last_inside for side_i in one_side):
                return one_inside
            else:
                return other_inside
        else:
            if any(side_i + delta_i in last_inside for side_i in other_side):
                return other_inside
            else:
                return one_inside
    else:
        if one_side:
            if any(side_i + delta_i in last_outside for side_i in one_side):
                return other_inside
            else:
                return one_inside
        else:
            if any(side_i + delta_i in last_outside for side_i in other_side):
                return one_inside
            else:
                return other_inside


def analyze_inside(pipes: list[Index], insides: list[list[Index]]) -> set[Index]:
    encs = set()
    for inside in insides:
        for ins in inside:
            if ins not in pipes:
                for adj in ADJECENT:
                    p = ins + adj
                    while p not in pipes:
                        encs.add(p)
                        p += adj
                encs.add(ins)
    return encs


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check_1(directory, solve_1):
        result = solve_1(load.inputs(directory))
        print(f"Result for inputs: {result}")

    if examples.check_2(directory, solve_2):
        result = solve_2(load.inputs(directory))
        print(f"Result for inputs: {result}")
