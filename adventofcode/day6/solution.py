import os
import math

from adventofcode import load, examples


def solve_1(inputs: list[str]) -> str:
    times = extract_values(inputs[0])
    distances = extract_values(inputs[1])
    races = [(t, d) for t, d in zip(times, distances)]
    product = 1
    for t, d in races:
        hold = breakpoint(t, d)
        ways_to_win = t - hold - hold + 1
        product *= ways_to_win
    return str(product)


def solve(inputs: list[str]) -> str:
    times = extract_values(inputs[0])
    distances = extract_values(inputs[1])
    time = int("".join([str(t) for t in times]))
    distance = int("".join([str(d) for d in distances]))
    product = 1
    hold = breakpoint(time, distance)
    ways_to_win = time - hold - hold + 1
    product *= ways_to_win
    return str(product)


def extract_values(line: str):
    return [int(n) for n in line.split(":")[1].strip().split(" ") if n]


def breakpoint(time: str, record: str) -> int:
    """
    Solves quadratic equation
    hold_time ** 2 - hold_time * total_time = distance_traveled
    set distance_traveled to record and solve for hold_time
    hold_time ** 2 - hold_time * total_time - record = 0
    curve is symmetric so only smaller solution is necessary
    """
    record_hold_time = (time - math.sqrt(time**2 - 4 * record)) / 2
    min_time_to_hold = math.ceil(record_hold_time)
    if min_time_to_hold == record_hold_time:
        min_time_to_hold += 1
    return min_time_to_hold


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check(directory, solve):
        result = solve(load.inputs(directory))
        print(f"Result for inputs: {result}")
