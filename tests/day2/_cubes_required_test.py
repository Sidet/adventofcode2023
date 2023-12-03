from unittest import TestCase

from adventofcode.day2 import solution as sol


class Test_cubes_required(TestCase):
    def s(self):
        actual = sol.cubes_found_in_set("Game1")
        self.assertEqual(expected, actual)
