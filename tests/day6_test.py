from unittest import TestCase

from adventofcode.day6 import solution as day


class Test_day6(TestCase):
    def test_breakpoint(self):
        actual = day.breakpoint(7, 9)
        self.assertEqual(2, actual)

    def test_breakpoint_record_matches_integer_hold_time(self):
        actual = day.breakpoint(30, 200)
        self.assertEqual(11, actual)

    def test_extract_values(self):
        actual = day.extract_values("Time:      7  15   30")
        self.assertEqual([7, 15, 30], actual)
