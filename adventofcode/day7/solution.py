import os
from collections import Counter

from adventofcode import load, examples


def solve(inputs: list[str]) -> str:
    bids_to_order = []
    for line in inputs:
        hand, bid_str = line.split()
        bid = int(bid_str)
        bids_to_order.append((hand_strength(hand), bid))
    bids_to_order.sort(key=lambda x: x[0])

    return str(sum(rank * bid for rank, (_, bid) in enumerate(bids_to_order, 1)))


def hand_type(hand: str):
    j_count = hand.count("J")
    hand = hand.replace("J", "")
    counter = Counter(hand)
    if counter:
        max_count = max(counter.values())
    else:
        max_count = 0
    max_count += j_count
    if max_count == 1:
        return "1"
    elif max_count == 2:
        if len(counter) == 4:
            return "2"
        else:
            return "3"
    elif max_count == 3:
        if len(counter) == 3:
            return "4"
        else:
            return "5"
    elif max_count == 4:
        return "6"
    else:
        return "7"


def card_order_value(card: str) -> str:
    if card.isdigit():
        return "0" + card
    elif card == "T":
        return "10"

    elif card == "J":
        return "01"

    elif card == "Q":
        return "12"

    elif card == "K":
        return "13"

    elif card == "A":
        return "14"


def hand_order_value(hand: str) -> str:
    return "".join(card_order_value(c) for c in hand)


def hand_strength(hand: str) -> str:
    return hand_type(hand) + hand_order_value(hand)


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check(directory, solve):
        result = solve(load.inputs(directory))
        print(f"Result for inputs: {result}")
