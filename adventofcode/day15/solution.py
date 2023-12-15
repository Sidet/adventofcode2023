import os
from collections import OrderedDict

from adventofcode import load, examples


def solve_1(inputs: list[str]) -> str:
    total = 0
    for line in inputs:
        for instruction in line.split(","):
            total += hash_(instruction)
    return str(total)


def solve_2(inputs: list[str]) -> str:
    boxes = [OrderedDict() for _ in range(256)]
    for line in inputs:
        for instruction in line.split(","):
            if "=" in instruction:
                label, focal_len = instruction.split("=")
                box = boxes[hash_(label)]
                box[label] = focal_len
            else:
                label = instruction[:-1]
                box = boxes[hash_(label)]
                if label in box:
                    del box[label]

    total_focal_power = 0
    for n, box in enumerate(boxes, 1):
        if box:
            for m, focal_len in enumerate(box.values(), 1):
                total_focal_power += n * m * int(focal_len)
    return str(total_focal_power)


def hash_(value: str) -> int:
    result = 0
    for v in value:
        result += ord(v)
        result *= 17
        result %= 256
    return result


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check_1(directory, solve_1):
        result = solve_1(load.inputs(directory))
        print(f"Result for inputs: {result}")

    if examples.check_2(directory, solve_2):
        result = solve_2(load.inputs(directory))
        print(f"Result for inputs: {result}")
