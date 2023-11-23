import unittest

from src.algorithms import convert_args_to_graph, get_minimum_beer_types_amount


class TestMinBeersFunction(unittest.TestCase):
    def test_two_employees_which_like_different_beers(self):
        beers_graph, workers_count = convert_args_to_graph("../input_2_workers.txt")
        result = get_minimum_beer_types_amount(beers_graph, workers_count)
        self.assertEqual(result, 2)

    def test_six_employees_3_beers(self):
        beers_graph, workers_count = convert_args_to_graph("../input_6_workers.txt")
        result = get_minimum_beer_types_amount(beers_graph, workers_count)
        self.assertEqual(result, 2)
