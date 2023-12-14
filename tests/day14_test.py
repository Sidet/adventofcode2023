from unittest import TestCase

from adventofcode.day14 import solution as day


class Test_day12(TestCase):
    def test_tilt_east(self):
        grid = [
            list("O......."),
            list("O....#.."),
            list("O.#OO.O#"),
        ]
        expected = [
            list(".......O"),
            list("....O#.."),
            list(".O#.OOO#"),
        ]
        day.tilt_east(grid)
        self.assertEqual(expected, grid)

    def test_rotate_clockwise(self):
        grid = [
            ["00", "01", "02", "03"],
            ["10", "11", "12", "13"],
            ["20", "21", "22", "23"],
            ["30", "31", "32", "33"],
        ]
        expected = [
            ["30", "20", "10", "00"],
            ["31", "21", "11", "01"],
            ["32", "22", "12", "02"],
            ["33", "23", "13", "03"],
        ]
        actual = day.rotate_clockwise(grid)
        self.assertEqual(expected, actual)
