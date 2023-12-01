
INPUT_FILE_PATH = "day1_puzzle2_input.txt"
NUMBER_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

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
    line_numbers = get_numerals_from_line(line)
    return int(str(line_numbers[0]) + str(line_numbers[-1]))

def get_numerals_from_line(line : str) -> list[int]:
    line = line.lower()
    numerals = []
    for i in range(0, len(line)):
        if line[i].isnumeric():
            numerals.append(int(line[i]))
            continue
        for number, word in enumerate(NUMBER_WORDS):
            if line[i:].startswith(word):
                numerals.append(number)
    
    return numerals

def get_calibration_sum_from_input_file() -> int:
    return get_calibration_sum_from_calibration_lines(get_calibration_lines_from_file(INPUT_FILE_PATH))

if __name__ == "__main__":
    print(get_calibration_sum_from_input_file())
