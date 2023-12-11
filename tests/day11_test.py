from unittest import TestCase

from adventofcode.day11 import solution as day


class Test_day11(TestCase):
    def test_count_numbers_between_4_numebers(self):
        numbers = [1, 2, 3, 5, 8, 10, 12, 14]
        actual = day.count_numbers_between(4, 11, numbers)
        self.assertEqual(3, actual)

    def test_count_numbers_between_0_numbers(self):
        numbers = [1, 2, 12, 14]
        actual = day.count_numbers_between(4, 11, numbers)
        self.assertEqual(0, actual)

    def test_count_numbers_between_1_number(self):
        numbers = [1, 2, 6, 12, 14]
        actual = day.count_numbers_between(4, 11, numbers)
        self.assertEqual(1, actual)

    def test_count_numbers_between_all_between(self):
        numbers = [2, 6, 8, 12, 14]
        actual = day.count_numbers_between(1, 15, numbers)
        self.assertEqual(5, actual)

    def test_count_numbers_between_all_bigger(self):
        numbers = [16, 18, 20]
        actual = day.count_numbers_between(1, 15, numbers)
        self.assertEqual(0, actual)

    def test_count_numbers_between_all_smaller(self):
        numbers = [1, 2, 3]
        actual = day.count_numbers_between(10, 15, numbers)
        self.assertEqual(0, actual)
