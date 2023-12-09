import os
from itertools import pairwise

from adventofcode import load, examples


class Sequence:
    def __init__(self, sequence: list[int]) -> None:
        self.derivative: list[list[int]] = []
        self.derivative.append(list(sequence))
        while any(v != 0 for v in self.derivative[-1]):
            self.derivative.append([b - a for a, b in pairwise(self.derivative[-1])])
        _ = self.derivative[-1] = [0]

    def __next__(self) -> int:
        for d1, d0 in pairwise(reversed(self.derivative)):
            d0.append(d1[-1] + d0[-1])
        return self.derivative[0][-1]

    def __repr__(self):
        return f"<{Sequence.__name__}(val={self.derivative[0][-1]})>"


class ReverseSequence(Sequence):
    def __init__(self, sequence: list[int]) -> None:
        super().__init__(sequence)
        for d in self.derivative:
            d.reverse()

    def __next__(self) -> int:
        for d1, d0 in pairwise(reversed(self.derivative)):
            d0.append(d0[-1] - d1[-1])
        return self.derivative[0][-1]

    def __repr__(self):
        return f"<{ReverseSequence.__name__}(val={self.derivative[0][-1]})>"


def solve_1(inputs: list[str]) -> str:
    sequences = [Sequence([int(v) for v in line.split()]) for line in inputs]
    total = 0
    for sequence in sequences:
        total += sequence.__next__()
    return str(total)


def solve_2(inputs: list[str]) -> str:
    sequences = [ReverseSequence([int(v) for v in line.split()]) for line in inputs]
    total = 0
    for sequence in sequences:
        total += sequence.__next__()
    return str(total)


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check_1(directory, solve_1):
        result = solve_1(load.inputs(directory))
        print(f"Result for inputs: {result}")

    if examples.check_2(directory, solve_2):
        result = solve_2(load.inputs(directory))
        print(f"Result for inputs: {result}")
