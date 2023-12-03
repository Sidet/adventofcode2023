import os

from . import names


def _inputs(path: str) -> list[str]:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def inputs(directory: str) -> list[str]:
    return _inputs(os.path.join(directory, names.INPUTS))


def example_inputs_1(directory: str) -> list[str]:
    return _inputs(os.path.join(directory, names.EXAMPLE1_INPUTS))


def example_inputs_2(directory: str) -> list[str]:
    return _inputs(os.path.join(directory, names.EXAMPLE2_INPUTS))


def _answer(path: str) -> str:
    with open(path, "r") as f:
        return f.readline().strip()


def example_answer_1(directory: str) -> str:
    return _answer(os.path.join(directory, names.EXAMPLE1_ANSWER))


def example_answer_2(directory: str) -> str:
    return _answer(os.path.join(directory, names.EXAMPLE2_ANSWER))
