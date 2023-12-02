import unittest
import day02_puzzle01

class Day02Puzzle01Test(unittest.TestCase):
    def setUp(self):
        self.given_input_game_lines = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]

    def test_given_example_get_game_from_string(self):
        self.assertEqual([day02_puzzle01.get_game_from_string(game_line) for game_line in self.given_input_game_lines], [
            (1, [{"red": 4, "blue": 3}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]),
            (2, [{"green": 2, "blue": 1}, {"red": 1, "green": 3, "blue": 4}, {"green": 1, "blue": 1}]),
            (3, [{"red": 20, "green": 8, "blue": 6}, {"red": 4, "green": 13, "blue": 5}, {"red": 1, "green": 5}]),
            (4, [{"red": 3, "green": 1, "blue": 6}, {"red": 6, "green": 3}, {"red": 14, "green": 3, "blue": 15}]),
            (5, [{"red": 6, "green": 3, "blue": 1}, {"red": 1, "green": 2, "blue": 2}])
        ])
    
    def test_given_example_calc_sum_of_game_numbers_from_games_filtered_by_max_cubes(self):
        self.assertEqual(
            day02_puzzle01.calc_sum_of_game_numbers_from_games_filtered_by_max_cubes(
                [day02_puzzle01.get_game_from_string(game_line) for game_line in self.given_input_game_lines],
                day02_puzzle01.get_cube_pull_from_string("12 red, 13 green, 14 blue")
            )
        , 8)
