from unittest import TestCase

from adventofcode.day8 import solution as day


class Test_day8(TestCase):
    def test_to_network(self):
        lines = [
            "AAA = (BBB, BBB)",
            "BBB = (AAA, ZZZ)",
            "ZZZ = (ZZZ, ZZZ)",
        ]
        expected = {
            "AAA": ("BBB", "BBB"),
            "BBB": ("AAA", "ZZZ"),
            "ZZZ": ("ZZZ", "ZZZ"),
        }
        actual = day.to_network(lines)
        self.assertEqual(
            expected,
            actual,
        )

    def test_to_indexes(self):
        directions = "RLLRL"
        expected = [1, 0, 0, 1, 0]
        actual = day.to_indexes(directions)
        self.assertEqual(expected, actual)
