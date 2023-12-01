import unittest
import day1_puzzle1

class Day1Puzzle1Test(unittest.TestCase):
    def setUp(self):
        self.given_input_calibration_lines = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet"
        ]

    def test_given_example_get_calibration_values_from_calibration_lines(self):
        self.assertEqual([day1_puzzle1.get_calibration_value_from_line(line) for line in self.given_input_calibration_lines], [12, 38, 15, 77])
    
    def test_given_example_get_calibration_sum_from_calibration_lines(self):
        self.assertEqual(day1_puzzle1.get_calibration_sum_from_calibration_lines(self.given_input_calibration_lines), 142)
