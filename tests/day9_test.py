from unittest import TestCase

from adventofcode.day9 import solution as day


class Test_day9(TestCase):
    def test_sequence_zeroth_derivative(self):
        line = [10, 13, 16, 21, 30, 45]
        sequence = day.Sequence(line)
        actual = sequence.derivative[0]
        self.assertEqual([10, 13, 16, 21, 30, 45], actual)

    def test_sequence_first_derivative(self):
        line = [10, 13, 16, 21, 30, 45]
        sequence = day.Sequence(line)
        actual = sequence.derivative[1]
        self.assertEqual([3, 3, 5, 9, 15], actual)

    def test_sequence_second_derivative(self):
        line = [10, 13, 16, 21, 30, 45]
        sequence = day.Sequence(line)
        actual = sequence.derivative[2]
        self.assertEqual([0, 2, 4, 6], actual)

    def test_sequence_third_derivative(self):
        line = [10, 13, 16, 21, 30, 45]
        sequence = day.Sequence(line)
        actual = sequence.derivative[3]
        self.assertEqual([2, 2, 2], actual)

    def test_sequence_next_value_simple_example(self):
        line = [10, 13, 16, 21, 30, 45]
        sequence = day.Sequence(line)
        actual = sequence.__next__()
        self.assertEqual(68, actual)
