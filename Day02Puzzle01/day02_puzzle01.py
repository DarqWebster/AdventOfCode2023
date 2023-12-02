
INPUT_FILE_PATH = "day02_puzzle01_input.txt"
MAX_CUBES_STRING = "12 red, 13 green, 14 blue"

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

def calc_sum_of_game_numbers_from_games_filtered_by_max_cubes(games : list[tuple[int, list[dict[str, int]]]], max_cubes : dict[str, int]) -> int:
    games = [game for game in games if is_cube_pull_list_possible(game[1], max_cubes)]
    return sum([game[0] for game in games])

def is_cube_pull_list_possible(cube_pull_list : list[dict[str, int]], max_cubes : dict[str, int]) -> bool:
    for cube_pull in cube_pull_list:
        if not is_cube_pull_possible(cube_pull, max_cubes):
            return False
    return True

def is_cube_pull_possible(cube_pull : dict[str, int], max_cubes : dict[str, int]) -> bool:
    for cube_type, cube_number in cube_pull.items():
        if cube_number > max_cubes.get(cube_type, 0):
            return False
    return True

# Execution.

def calc_sum_of_game_numbers_from_games_filtered_by_max_cubes_from_input_file() -> int:
    games = [get_game_from_string(game_line) for game_line in get_game_lines_from_file(INPUT_FILE_PATH)]
    max_cubes = get_cube_pull_from_string(MAX_CUBES_STRING)

    return calc_sum_of_game_numbers_from_games_filtered_by_max_cubes(games, max_cubes)

if __name__ == "__main__":
    print(calc_sum_of_game_numbers_from_games_filtered_by_max_cubes_from_input_file())
