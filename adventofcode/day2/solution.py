import os
from collections import defaultdict

from adventofcode import load, examples

cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def solve(inputs: list[str]) -> str:
    total = 0
    for line in inputs:
        gamename, sets = line.split(": ")
        sets = sets.split("; ")

        cubes_found = cubes_found_in_sets(sets)

        total += game_powerset(cubes_found)
    return str(total)


def cubes_found_in_sets(sets):
    cubes_found: dict[str, list[int]] = defaultdict(list)
    for s in sets:
        found = cubes_found_in_set(s)
        for name, quantity in found.items():
            cubes_found[name].append(quantity)
    return cubes_found


def cubes_found_in_set(game_set: str) -> dict[str, int]:
    cubes = game_set.split(", ")
    required = {}
    for c in cubes:
        quantity, color = c.split(" ")
        quantity = int(quantity)
        required[color] = quantity
    return required


def game_is_possible(cubes_found: dict[str, list[int]]) -> bool:
    for color, quantity in cubes.items():
        if quantity < max(cubes_found[color]):
            return False
    return True


def game_powerset(cubes_found: dict[str, list[int]]) -> int:
    powerset = 1
    for quantities in cubes_found.values():
        powerset *= max(quantities)
    return powerset


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check(directory, solve):
        result = solve(load.inputs(directory))
        print(f"Result for inputs: {result}")
