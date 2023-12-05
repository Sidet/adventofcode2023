from __future__ import annotations

import os
from collections import defaultdict
from itertools import pairwise, batched

from adventofcode import load, examples


class Range:
    """end is not inclusive"""

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def length(self):
        return self.end - self.start

    def __sub__(self, other: Range) -> list[Range]:
        if other.end <= self.start or self.end <= other.start:
            return [Range(self.start, self.end)]
        else:
            ranges: list[Range] = [
                Range(self.start, max(self.start, other.start)),
                Range(min(self.end, other.end), self.end),
            ]
            return [r for r in ranges if r.length()]

    def overlap(self, other: Range) -> Range:
        if other.end <= self.start or self.end <= other.start:
            return None
        else:
            return Range(max(self.start, other.start), min(self.end, other.end))

    def __repr__(self):
        return f"<Range({self.start}, {self.end})>"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Range):
            return self.start == __value.start and self.end == __value.end


class Converter:
    def __init__(self) -> None:
        self._ranges: list[tuple(Range, int)] = []

    def __getitem__(self, value: Range) -> list[tuple[int, int]]:
        remainder = [value]
        ranges = []
        for source, dest in self._ranges:
            other = []
            for r in remainder:
                overlap = r.overlap(source)
                other.extend(r - source)
                if overlap:
                    start = overlap.start - source.start + dest
                    ranges.append(Range(start, start + overlap.length()))
            remainder = other
        return ranges + remainder

    def addrange(self, destination: int, source: int, count: int):
        self._ranges.append((Range(source, source + count), destination))


def solve_1(inputs: list[str]) -> str:
    seeds = to_seeds_1(inputs[0])
    raw_mappings = split_into_mappings(inputs)
    mapping: dict[str, dict[str, dict[int, int]]] = defaultdict(dict)
    for raw in raw_mappings:
        source, dest = name_to_sources(raw[0])
        mapping[source][dest] = to_converter(raw[1:])
    locations = []
    for seed, n in seeds:
        locations.append(a_to_b("seed", "location", seed, mapping))
    return str(min(locations))


def solve(inputs: list[str]) -> str:
    seeds = to_seeds(inputs[0])
    raw_mappings = split_into_mappings(inputs)
    mapping: dict[str, dict[str, dict[int, int]]] = defaultdict(dict)
    for raw in raw_mappings:
        source, dest = name_to_sources(raw[0])
        mapping[source][dest] = to_converter(raw[1:])
    locations = []
    for seed in seeds:
        for location in a_to_b("seed", "location", seed, mapping):
            locations.append(location)
    return str(min(n.start for n in locations))


def to_seeds_1(raw_seeds: str) -> list[tuple[int, int]]:
    return [(int(n), 1) for n in raw_seeds.split(": ")[1].split(" ")]


def to_seeds(raw_seeds: str) -> list[tuple[int, int]]:
    return [
        Range(int(n), int(n) + int(m))
        for n, m in batched(raw_seeds.split(": ")[1].split(" "), 2)
    ]


def split_into_mappings(raw: list[str]) -> list[list[str]]:
    raw_mappings: list[list[str]] = []
    mapping = []
    for line in raw:
        if line:
            if mapping or "-" in line:
                mapping.append(line)
        else:
            if mapping:
                raw_mappings.append(mapping)
            mapping = []
    if mapping:
        raw_mappings.append(mapping)
    return raw_mappings


def to_converter(raw: list[str]) -> Converter:
    converter = Converter()
    for r in raw:
        converter.addrange(*[int(n) for n in r.split(" ")])
    return converter


def name_to_sources(name: str) -> list[str]:
    return name.split(" ")[0].split("-to-")


def a_to_b(
    source: str,
    destination: str,
    number: Range,
    mapping: dict[str, dict[str, dict[int, int]]],
) -> list[Range]:
    path = find_convertions_path(source, destination, mapping)
    ranges = [number]
    for s, d in pairwise(path):
        converter = mapping[s][d]
        converted = [converter[r] for r in ranges]
        ranges = [b for a in converted for b in a]
    return ranges


def find_convertions_path(
    source: str,
    destination: str,
    mapping: dict[str, dict[str, dict[int, int]]],
) -> list[str]:
    if source in mapping:
        if destination in mapping[source]:
            return [source, destination]
        else:
            for possible_source in mapping[source]:
                path = find_convertions_path(possible_source, destination, mapping)
                if path:
                    return [source] + path
    return None


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    if examples.check(directory, solve):
        result = solve(load.inputs(directory))
        print(f"Result for inputs: {result}")
