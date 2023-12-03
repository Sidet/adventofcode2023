import os
from itertools import pairwise

from . import names


def empty_day(directory: str, name: str) -> None:
    dir = os.path.join(directory, name)
    os.mkdir(dir)
    create_empty_file(os.path.join(dir, names.INIT))
    copy_solutionbase(directory, dir)
    create_empty_file(os.path.join(dir, names.INPUTS))
    create_empty_file(os.path.join(dir, names.EXAMPLE1_INPUTS))
    create_empty_file(os.path.join(dir, names.EXAMPLE1_ANSWER))
    create_empty_file(os.path.join(dir, names.EXAMPLE2_INPUTS))
    create_empty_file(os.path.join(dir, names.EXAMPLE2_ANSWER))


def create_empty_file(path: str):
    with open(path, "w"):
        pass


def copy_solutionbase(source_dir: str, destination_dir: str):
    with open(os.path.join(source_dir, names.SOLUTIONBASE), "r") as f:
        lines = f.readlines()
    with open(os.path.join(destination_dir, names.SOLUTION), "w") as f:
        f.writelines(lines)


def nextdayname(directory: str) -> str:
    days_numbers = []
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isdir(path) and name.startswith(names.DAY_STARTSWITH):
            try:
                number = (int)(name[len(names.DAY_STARTSWITH) :])
                days_numbers.append(number)
            except:
                pass

    return f"{names.DAY_STARTSWITH}{_first_unused_number(days_numbers)}"


def _first_unused_number(numbers: list[int]) -> int:
    numbers.sort()
    if len(numbers) == 0 or numbers[0] != 1:
        return 1
    for a, b in pairwise(numbers):
        if a + 1 != b:
            return a + 1
    return numbers[-1] + 1


def new_day(directory: str) -> str:
    name = nextdayname(directory)
    empty_day(directory, name)
    return name


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    name = new_day(directory)
    print(f"{name} setup.")
