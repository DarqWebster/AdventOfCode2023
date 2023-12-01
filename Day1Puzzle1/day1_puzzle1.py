
INPUT_FILE_PATH = "day1_puzzle1_input.txt"

def get_calibration_lines_from_file(file_path : str) -> list[str]:
    with open(file_path, "r") as file_i:
        return file_i.readlines()

def get_calibration_sum_from_calibration_lines(calibration_lines : list[str]) -> int:
    calibration_values = [get_calibration_value_from_line(line) for line in calibration_lines]
    calibration_sum = 0
    for value in calibration_values:
        calibration_sum += value
    return calibration_sum

def get_calibration_value_from_line(line : str) -> int:
    line_numbers = [char for char in line if char.isnumeric()]
    return int(line_numbers[0] + line_numbers[-1])

def get_calibration_sum_from_input_file() -> int:
    return get_calibration_sum_from_calibration_lines(get_calibration_lines_from_file(INPUT_FILE_PATH))

if __name__ == "__main__":
    print(get_calibration_sum_from_input_file())
