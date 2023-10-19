import unittest

from algorithms import get_min_desk_length


class TestMinimumLength(unittest.TestCase):
    def test_from_example(self):
        expected_result = 9
        actual_result = get_min_desk_length(10, 2, 3)
        self.assertEqual(expected_result, actual_result)

    def test_wrong_args(self):
        expected_result = -1
        actual_result = get_min_desk_length(12, 130, 12)
        self.assertEqual(expected_result, actual_result)

    def test_square_sheets(self):
        expected_result = 6
        actual_result = get_min_desk_length(8, 2, 2)
        self.assertEqual(expected_result, actual_result)
