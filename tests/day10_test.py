from unittest import TestCase

from adventofcode.day10 import solution as day


class Test_day10(TestCase):
    def test_to_grid(self):
        inputs = [".......", ".......", "......."]
        expected = [["."] * 7] * 3
        actual = day.to_grid(inputs)
        self.assertEqual(expected, actual)

    def test_start_index(self):
        grid = [
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", "S", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
        ]
        actual = day.start_index(grid).to_tuple()
        expected = (2, 3)
        self.assertEqual(expected, actual)

    def test_pipe_exits_vertical(self):
        actual = day.pipe_exits(day.Index(3, 3), "|")
        expected = ((2, 3), (4, 3))
        self.assertEqual(expected, actual)

    def test_pipe_exits_horizontal(self):
        actual = day.pipe_exits(day.Index(3, 3), "-")
        expected = ((3, 2), (3, 4))
        self.assertEqual(expected, actual)

    def test_pipe_exits_F(self):
        actual = day.pipe_exits(day.Index(3, 3), "F")
        expected = ((4, 3), (3, 4))
        self.assertEqual(expected, actual)

    def test_pipe_exits_J(self):
        actual = day.pipe_exits(day.Index(3, 3), "J")
        expected = ((2, 3), (3, 2))
        self.assertEqual(expected, actual)

    def test_pipe_exits_7(self):
        actual = day.pipe_exits(day.Index(3, 3), "7")
        expected = ((3, 2), (4, 3))
        self.assertEqual(expected, actual)

    def test_pipe_exits_L(self):
        actual = day.pipe_exits(day.Index(3, 3), "L")
        expected = ((2, 3), (3, 4))
        self.assertEqual(expected, actual)

    def test_adjecents(self):
        actual = set(day.adjecents(day.Index(2, 3)))
        expected = set([(1, 3), (2, 4), (3, 3), (2, 2)])
        self.assertEqual(expected, actual)

    def test_exits_from_start(self):
        grid = [
            [".", "F", "."],
            ["7", "S", "|"],
            [".", "J", "."],
        ]
        actual = list(day.exits_from_start(day.Index(1, 1), grid))
        expected = [(0, 1), (2, 1)]
        self.assertEqual(expected, actual)

    def test_next_pipe(self):
        expected = (1, 4)
        actual = day.next_pipe(day.Index(2, 3), day.Index(2, 4), "J")
        self.assertEqual(expected, actual)

    def test_enclosed_simple_loop(self):
        inputs = [
            "F-7",
            "S.|",
            "L-J",
        ]
        expected = "1"
        actual = day.solve_2(inputs)
        self.assertEqual(expected, actual)

    def test_enclosures_loop_with_extra(self):
        inputs = [
            "......",
            "..F7..",
            ".FJ|..",
            ".S.L7.",
            ".L-7|.",
            "...LJ.",
            "......",
        ]
        expected = "1"
        actual = day.solve_2(inputs)
        self.assertEqual(expected, actual)
