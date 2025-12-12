import numpy as np
from pathlib import Path
from typing import List

INPUT_PATH = Path("./input.txt")

input_list:List[str] = []

with open(INPUT_PATH) as file:
    for line in file:
        input_list.append(line.strip())



number_elements:int = len(input_list[0])
rolls_symbol:str = "@"
total_of_rolls_symbol:int = 0

matrix = np.array([list(row) for row in input_list])


for raw_index, raw_list in enumerate(matrix):
    print(raw_index, raw_list)
    for val_index, list_element in enumerate(raw_list):
        print(val_index, list_element)
        if list_element == rolls_symbol:
            if val_index > 0:
                left_element = matrix[raw_index][val_index-1]
            if val_index < number_elements-1:
                right_element = matrix[raw_index][val_index+1]
                print(right_element)







        # if list_element == rolls_symbol:
        #     left_rng_for_check = raw_list[0: val_index]
        #     left_count_of_rolls_symbol = (np.count_nonzero(left_rng_for_check[-8:] == rolls_symbol))
        #     right_rng_for_check = raw_list[val_index+1:]
        #     right_count_of_rolls_symbol = (np.count_nonzero(right_rng_for_check[:8] == rolls_symbol))
        #     print(right_count_of_rolls_symbol)


            # if left_count_of_rolls_symbol <5: #and right_count_of_rolls_symbol <5:
            #     total_of_rolls_symbol +=1

            #print(total_of_rolls_symbol)


