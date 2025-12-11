import numpy as np
from pathlib import Path
from typing import List

INPUT_PATH = Path("./input.txt")

input_list:List[str] = []

with open(INPUT_PATH) as file:
    for line in file:
        input_list.append(line.strip())


number_of_positions:int = 8
number_elements:int = len(input_list[0])
index:int = 0

matrix2 = np.array([list(row) for row in input_list])


for raw_index, raw_list in enumerate(matrix2):
    print(raw_index, raw_list)
    for val_index, list_element in enumerate(raw_list):
        if list_element == "@":
            pass

