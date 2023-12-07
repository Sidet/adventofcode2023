from unittest import TestCase

from adventofcode.day7 import solution as day


class Test_hand_type(TestCase):
    def test_is_1(self):
        actual = day.hand_type("42T3K")
        self.assertEqual("1", actual)

    def test_is_2(self):
        actual = day.hand_type("423JQ")
        self.assertEqual("2", actual)

    def test_is_3(self):
        actual = day.hand_type("233QQ")
        self.assertEqual("3", actual)

    def test_is_4(self):
        actual = day.hand_type("23J34")
        self.assertEqual("4", actual)

    def test_is_5(self):
        actual = day.hand_type("2233J")
        self.assertEqual("5", actual)

    def test_is_6(self):
        actual = day.hand_type("QQJQ4")
        self.assertEqual("6", actual)

    def test_is_7(self):
        actual = day.hand_type("AAAJA")
        self.assertEqual("7", actual)


class Test_card_order_value(TestCase):
    def test_2(self):
        actual = day.card_order_value("2")
        self.assertEqual("02", actual)

    def test_T(self):
        actual = day.card_order_value("T")
        self.assertEqual("10", actual)

    def test_J(self):
        actual = day.card_order_value("J")
        self.assertEqual("01", actual)

    def test_Q(self):
        actual = day.card_order_value("Q")
        self.assertEqual("12", actual)

    def test_K(self):
        actual = day.card_order_value("K")
        self.assertEqual("13", actual)

    def test_A(self):
        actual = day.card_order_value("A")
        self.assertEqual("14", actual)
