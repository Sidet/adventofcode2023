from unittest import TestCase

from adventofcode.day5 import solution as day


class Test_a(TestCase):
    def test_name_to_sources(self):
        mapping_name = "seed-to-soil map:"
        actual = day.name_to_sources(mapping_name)
        self.assertEqual(["seed", "soil"], actual)

    def test_seeds_1(self):
        line = "seeds: 79 14 55 13"
        actual = day.to_seeds_1(line)
        self.assertEqual(set([(79, 1), (14, 1), (55, 1), (13, 1)]), set(actual))

    def test_seeds(self):
        line = "seeds: 79 14 55 13"
        actual = day.to_seeds(line)
        self.assertEqual([day.Range(79, 79 + 14), day.Range(55, 55 + 13)], actual)

    def test_split_into_mappings(self):
        raw = [
            "seeds: 79 14 55 13",
            "",
            "seed-to-soil map:",
            "50 98 2",
            "52 50 48",
            "",
            "soil-to-fertilizer map:",
            "0 15 37",
            "37 52 2",
            "39 0 15",
            "",
        ]
        expected = [
            [
                "seed-to-soil map:",
                "50 98 2",
                "52 50 48",
            ],
            [
                "soil-to-fertilizer map:",
                "0 15 37",
                "37 52 2",
                "39 0 15",
            ],
        ]
        actual = day.split_into_mappings(raw)
        self.assertEqual(expected, actual)

    def test_a_to_b(self):
        converter1 = day.Converter()
        converter1.addrange(2, 1, 1)
        converter2 = day.Converter()
        converter2.addrange(3, 2, 1)
        mapping = {"a": {"b": converter1}, "b": {"c": converter2}}
        actual = day.a_to_b("a", "c", day.Range(1, 2), mapping)
        self.assertEqual([day.Range(3, 4)], actual)

    def test_a_to_b_4_steps_no_convertions(self):
        mapping = {
            "a": {"b": day.Converter()},
            "b": {"c": day.Converter()},
            "c": {"d": day.Converter()},
            "d": {"e": day.Converter()},
        }
        actual = day.a_to_b("a", "e", day.Range(6, 7), mapping)
        self.assertEqual([day.Range(6, 7)], actual)

    def test_find_convertions_path_direct(self):
        mapping = {"a": {"b": {}}, "b": {"c": {}}}
        actual = day.find_convertions_path("a", "b", mapping)
        self.assertEqual(["a", "b"], actual)

    def test_find_convertions_path_2_steps(self):
        mapping = {"a": {"b": {}}, "b": {"c": {}}}
        actual = day.find_convertions_path("a", "c", mapping)
        self.assertEqual(["a", "b", "c"], actual)

    def test_find_convertions_path_4_steps(self):
        mapping = {"a": {"b": {}}, "b": {"c": {}}, "c": {"d": {}}, "d": {"e": {}}}
        actual = day.find_convertions_path("a", "e", mapping)
        self.assertEqual(["a", "b", "c", "d", "e"], actual)


class TestConverter(TestCase):
    def test_get_item_no_ranges(self):
        converter = day.Converter()
        actual = converter[day.Range(5, 6)]
        self.assertEqual([day.Range(5, 6)], actual)

    def test_get_item_1_length_range(self):
        converter = day.Converter()
        converter.addrange(2, 1, 1)
        actual = converter[day.Range(1, 2)]
        self.assertEqual([day.Range(2, 3)], actual)

    def test_get_item_long_range(self):
        converter = day.Converter()
        converter.addrange(1, 11, 999999)
        actual = converter[day.Range(1000000, 1000001)]
        self.assertEqual([day.Range(999990, 999991)], actual)


class TestRange(TestCase):
    def test_sub_ranges_do_not_ovelap_returns_copy_of_a(self):
        a = day.Range(10, 20)
        b = day.Range(30, 40)
        actual = a - b
        self.assertEqual([a], actual)

    def test_sub_a_encompassed_by_b_returns_empty_list(self):
        a = day.Range(10, 20)
        b = day.Range(5, 25)
        actual = a - b
        self.assertEqual([], actual)

    def test_sub_a_overlaps_b_return_list_with_one_element(self):
        a = day.Range(10, 20)
        b = day.Range(15, 25)
        actual = a - b
        self.assertEqual([day.Range(10, 15)], actual)

    def test_sub_a_overlaps_b_return_list_with_two_elements(self):
        a = day.Range(10, 20)
        b = day.Range(12, 18)
        actual = a - b
        self.assertEqual([day.Range(10, 12), day.Range(18, 20)], actual)

    def test_overlap_ranges_do_not_ovelap_returns_None(self):
        a = day.Range(10, 20)
        b = day.Range(30, 40)
        actual = a.overlap(b)
        self.assertEqual(None, actual)

    def test_overlap_a_encompassed_by_b_returns_copy_of_a(self):
        a = day.Range(10, 20)
        b = day.Range(5, 25)
        actual = a.overlap(b)
        self.assertEqual(a, actual)

    def test_overlap_a_partial_overlap_b(self):
        a = day.Range(10, 20)
        b = day.Range(15, 25)
        actual = a.overlap(b)
        self.assertEqual(day.Range(15, 20), actual)

    def test_overlap_a_encompasses_b_return_copy_of_b(self):
        a = day.Range(10, 20)
        b = day.Range(12, 18)
        actual = a.overlap(b)
        self.assertEqual(day.Range(12, 18), actual)
