import os
from itertools import cycle, batched
from adventofcode import load, examples


class Sequence:
    def __init__(self, steps: list[int]) -> None:
        self.i = 0
        self._steps = steps
        self._limit = len(self._steps) - 1
        self.current = self._steps[self.i]

    def __next__(self):
        if self.i == self._limit:
            self.current += self._steps[-1]
        else:
            self.i += 1
            self.current += self._steps[self.i]

    def __repr__(self) -> str:
        return f"<{Sequence.__name__}(steps={self.current})>"


def solve_1(inputs: list[str]) -> str:
    directions = to_indexes(inputs[0])
    network = to_network(inputs[2:])
    steps = 0
    node = "AAA"
    for direction in cycle(directions):
        steps += 1
        node = network[node][direction]
        if node == "ZZZ":
            break

    return str(steps)


def solve_2(inputs: list[str]) -> str:
    directions = to_indexes(inputs[0])
    network = to_network(inputs[2:])
    nodes = [n for n in network.keys() if n.endswith("A")]
    initial_sequences = []
    for node in nodes:
        steps = []
        current = 0
        last_steps = 0
        for direction in cycle(directions):
            current += 1
            node = network[node][direction]
            if node.endswith("Z"):
                steps.append(current - last_steps)
                last_steps = current
            if len(steps) > 4 and all(steps[-1] == s for s in steps[-4:]):
                break
        initial_sequences.append(steps)

    seqences = [Sequence(n) for n in initial_sequences]
    next_group: list[Sequence] = []
    while len(seqences) > 1:
        next_group: list[Sequence] = []
        for batch in batched(seqences, 2):
            if len(batch) == 2:
                next_group.append(combine_sequences(*batch))
            else:
                next_group.insert(0, batch[0])
        seqences = next_group

    return str(seqences[0].current)


def combine_sequences(sq1: Sequence, sq2: Sequence) -> Sequence:
    steps = []
    while True:
        if sq1.current == sq2.current:
            steps.append(sq1.current)
            if len(steps) > 4 and all(steps[-1] == s for s in steps[-4:]):
                break
        elif sq1.current < sq2.current:
            sq1.__next__()
        else:
            sq2.__next__()
    return Sequence(steps)


def to_network(lines: str) -> dict[str, tuple[str, str]]:
    network: dict[str, tuple[str, str]] = {}
    for line in lines:
        name, branches = line.split(" = ")
        network[name] = tuple(b for b in branches[1:-1].split(", "))
    return network


def to_indexes(directions: str) -> list[int]:
    return [to_index(d) for d in directions]


def to_index(direction: str) -> int:
    if direction == "L":
        return 0
    else:
        return 1


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check_1(directory, solve_1):
        result = solve_1(load.inputs(directory))
        print(f"Result 1 for inputs: {result}")

    if examples.check_2(directory, solve_2):
        result = solve_2(load.inputs(directory))
        print(f"Result 2 for inputs: {result}")
