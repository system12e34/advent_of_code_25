import numpy as np
from pathlib import Path
from typing import List, Tuple

INPUT_PATH = Path("./input.txt")

input_list:List[str] = []

with open(INPUT_PATH) as file:
    for line in file:
        input_list.append(line.strip())


number_cols: int = len(input_list[0])
number_raws: int = len(input_list)
rolls_symbol: str = "@"
total_of_rolls_symbol: int = 0
number_rolls_for_element: int = 0
positions_to_remove: List[Tuple[int, int]] = []
retry_finding_rolls: bool = True
matrix = np.array([list(row) for row in input_list])



while retry_finding_rolls:
    for raw_index, raw_list in enumerate(matrix):
        for val_index, list_element in enumerate(raw_list):
            number_rolls_for_element = 0
            if list_element == rolls_symbol:
                if val_index > 0:
                    left_element = matrix[raw_index][val_index-1]
                    if left_element == rolls_symbol:
                        number_rolls_for_element += 1
                if val_index < number_cols-1:
                    right_element = matrix[raw_index][val_index+1]
                    if right_element == rolls_symbol:
                        number_rolls_for_element += 1
                if raw_index > 0:
                    upper_element = matrix[raw_index-1][val_index]
                    if upper_element == rolls_symbol:
                        number_rolls_for_element += 1
                if raw_index < number_raws-1:
                    lower_element = matrix[raw_index+1][val_index]
                    if lower_element == rolls_symbol:
                        number_rolls_for_element += 1
                if raw_index > 0 and val_index > 0:
                    upper_left_element = matrix[raw_index-1][val_index-1]
                    if upper_left_element == rolls_symbol:
                        number_rolls_for_element += 1
                if raw_index > 0 and val_index < number_cols-1:
                    upper_right_element = matrix[raw_index-1][val_index+1]
                    if upper_right_element == rolls_symbol:
                        number_rolls_for_element += 1
                if raw_index < number_raws-1 and val_index > 0:
                    lower_left_element = matrix[raw_index+1][val_index-1]
                    if lower_left_element == rolls_symbol:
                        number_rolls_for_element += 1
                if raw_index < number_raws-1 and val_index < number_cols-1:
                    lower_right_element = matrix[raw_index+1][val_index+1]
                    if lower_right_element == rolls_symbol:
                        number_rolls_for_element += 1
                if number_rolls_for_element < 4:
                    total_of_rolls_symbol += 1
                    positions_to_remove.append((raw_index, val_index))

    if len(positions_to_remove) > 0:
            for position in positions_to_remove:
                matrix[position[0]][position[1]] = "."
            positions_to_remove = []
    else:
        retry_finding_rolls = False


print(total_of_rolls_symbol)
