import unittest
import day1_puzzle2

class Day1Puzzle2Test(unittest.TestCase):
    def setUp(self):
        self.given_input_calibration_lines = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen"
        ]
        self.overlapping_calibration_lines = [
            "zerone",
            "oneight",
            "twone",
            "threeight",
            "fiveight",
            "sevenine",
            "eightwo",
            "eighthree",
            "nineight",
            "zeroneight",
            "oneightwo"
        ]
        self.overlapping_not_start_or_end_calibration_lines = [
            "xzeronex",
            "xoneightx",
            "xtwonex",
            "xthreeightx",
            "xfiveightx",
            "xseveninex",
            "xeightwox",
            "xeighthreex",
            "xnineightx",
            "xzeroneightx",
            "xoneightwox"
        ]

    def test_given_example_get_numerals_from_line(self):
        self.assertEqual([day1_puzzle2.get_numerals_from_line(line) for line in self.given_input_calibration_lines], [
            [2, 1, 9],
            [8, 2, 3],
            [1, 2, 3],
            [2, 1, 3, 4],
            [4, 9, 8, 7, 2],
            [1, 8, 2, 3, 4],
            [7, 6]
        ])

    def test_given_example_get_calibration_values_from_calibration_lines(self):
        self.assertEqual([day1_puzzle2.get_calibration_value_from_line(line) for line in self.given_input_calibration_lines], [
            29,
            83,
            13,
            24,
            42,
            14,
            76
        ])
    
    def test_given_example_get_calibration_sum_from_calibration_lines(self):
        self.assertEqual(day1_puzzle2.get_calibration_sum_from_calibration_lines(self.given_input_calibration_lines), 281)

    def test_get_numerals_from_line_overlapping(self):
        self.assertEqual([day1_puzzle2.get_numerals_from_line(line) for line in self.overlapping_calibration_lines], [
            [0, 1],
            [1, 8],
            [2, 1],
            [3, 8],
            [5, 8],
            [7, 9],
            [8, 2],
            [8, 3],
            [9, 8],
            [0, 1, 8],
            [1, 8, 2]
        ])

    def test_get_calibration_values_from_calibration_lines_overlapping(self):
        self.assertEqual([day1_puzzle2.get_calibration_value_from_line(line) for line in self.overlapping_calibration_lines], [
            1,
            18,
            21,
            38,
            58,
            79,
            82,
            83,
            98,
            8,
            12
        ])
    
    def test_get_numerals_from_line_overlapping_not_start_or_end_of_line(self):
        self.assertEqual([day1_puzzle2.get_numerals_from_line(line) for line in self.overlapping_not_start_or_end_calibration_lines], [
            [0, 1],
            [1, 8],
            [2, 1],
            [3, 8],
            [5, 8],
            [7, 9],
            [8, 2],
            [8, 3],
            [9, 8],
            [0, 1, 8],
            [1, 8, 2]
        ])
    
    def test_get_calibration_values_from_calibration_lines_overlapping_not_start_or_end_of_line(self):
        self.assertEqual([day1_puzzle2.get_calibration_value_from_line(line) for line in self.overlapping_not_start_or_end_calibration_lines], [
            1,
            18,
            21,
            38,
            58,
            79,
            82,
            83,
            98,
            8,
            12
        ])
