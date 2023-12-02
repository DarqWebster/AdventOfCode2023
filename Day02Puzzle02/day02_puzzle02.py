from functools import reduce

INPUT_FILE_PATH = "day02_puzzle02_input.txt"

# IO and Parsing.

def get_game_lines_from_file(file_path : str) -> list[str]:
    with open(file_path, "r") as file_i:
        return file_i.readlines()

def get_game_from_string(game_string : str) -> tuple[int, list[dict[str, int]]]:
    game_number_string, cube_pull_list_string = game_string.split(": ")
    game_number = int(game_number_string[5:])
    cube_pull_list = [get_cube_pull_from_string(cube_pull_string) for cube_pull_string in cube_pull_list_string.split("; ")]
    return game_number, cube_pull_list

def get_cube_pull_from_string(cube_pull_string : str) -> dict[str, int]:
    cube_pull = {}
    for cube_number_type_string in cube_pull_string.strip().split(", "):
        cube_number, cube_type = cube_number_type_string.strip().split(" ")
        cube_pull[cube_type] = int(cube_number)
    return cube_pull

# Calculations.

def calc_sum_of_powers_of_min_cubes_of_games(games : list[tuple[int, list[dict[str, int]]]]) -> int:
    return sum([
        reduce(lambda x, y: x*y, get_min_cubes(game[1]).values(), 1)
        for game in games
    ])

def get_min_cubes(cube_pull_list : list[dict[str, int]]) -> dict[str, int]:
    min_cubes = {}
    for cube_pull in cube_pull_list:
        for cube_type, cube_number in cube_pull.items():
            if min_cubes.get(cube_type, 0) < cube_number:
                min_cubes[cube_type] = cube_number
    return min_cubes

# Execution.

def calc_sum_of_powers_of_min_cubes_of_games_from_input_file() -> int:
    games = [get_game_from_string(game_line) for game_line in get_game_lines_from_file(INPUT_FILE_PATH)]

    return calc_sum_of_powers_of_game_min_cubes(games)

if __name__ == "__main__":
    print(calc_sum_of_powers_of_min_cubes_of_games_from_input_file())
