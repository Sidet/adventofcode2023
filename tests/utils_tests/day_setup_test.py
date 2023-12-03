from unittest import TestCase

import adventofcode.day_setup as ds


class Test_first_unused_number(TestCase):
    def test_empty_list(self):
        actual = ds._first_unused_number([])
        self.assertEqual(1, actual)

    def test_gap_in_numbers(self):
        actual = ds._first_unused_number([1, 2, 3, 5, 6])
        self.assertEqual(4, actual)

    def test_numbers_start_from_2(self):
        actual = ds._first_unused_number([2, 3, 5, 6])
        self.assertEqual(1, actual)

    def test_numbers_in_order(self):
        actual = ds._first_unused_number([1, 2, 3])
        self.assertEqual(4, actual)
