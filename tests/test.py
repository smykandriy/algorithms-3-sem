import unittest

from src.kmp import kmp_search


class TestKMPSearch(unittest.TestCase):
    def test_multiple_needles(self):
        expected_result = [(3, 7), (10, 14)]
        actual_result = kmp_search("ABABAABBABBAAB", "BAAB")
        self.assertEqual(expected_result, actual_result)

    def test_one_needle(self):
        expected_result = [(9, 13)]
        actual_result = kmp_search("ABABABBABBAAB", "BAAB")
        self.assertEqual(expected_result, actual_result)

    def test_needle_not_found(self):
        expected_result = [(-1, -1)]
        actual_result = kmp_search("ABABABBABBAAB", "FFFF")
        self.assertEqual(expected_result, actual_result)
