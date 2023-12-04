import os
from collections import defaultdict

from adventofcode import load, examples


def solve_1(inputs: list[str]) -> str:
    total = 0
    for card in inputs:
        _, numbers = card.split(": ")
        winning, present = numbers.split(" | ")
        winning = [n.strip() for n in winning.split(" ") if n.strip()]
        present = [n.strip() for n in present.split(" ") if n.strip()]
        matches = len(set(winning).intersection(present))
        if matches:
            total += int(2 ** (matches - 1))
    return str(total)


def solve(inputs: list[str]) -> str:
    card_counts: dict[str, int] = defaultdict(lambda: 0)
    for n, card in enumerate(inputs, 1):
        card_counts[n] += 1
        _, numbers = card.split(": ")
        winning, present = numbers.split(" | ")
        winning = [n.strip() for n in winning.split(" ") if n.strip()]
        present = [n.strip() for n in present.split(" ") if n.strip()]
        matches = len(set(winning).intersection(present))
        addcards(n, matches, card_counts)
    return str(sum(v for v in card_counts.values()))


def addcards(current: int, matches: int, card_counts: dict[str, int]):
    cards = card_counts[current]
    for n in range(current + 1, current + matches + 1):
        card_counts[n] += cards


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check(directory, solve):
        result = solve(load.inputs(directory))
        print(f"Result for inputs: {result}")
