from pathlib import Path
from typing import List

INPUT_PATH = Path("./input.txt")

input_list:List[str] = []
sum_pairs:int = 0


with open(INPUT_PATH) as file:
    for line in file:
        input_list.append(line.strip())


for i in input_list:
    n = len(i)
    list_with_biggest_joltage = []
    start_index = 0
    remaining_digits_to_select = 12

    while remaining_digits_to_select > 0:
        best_digit = "-1"
        last_index_to_start = n - remaining_digits_to_select
        best_position = start_index

        #Max between start index and last_index_to_start
        for j in range(start_index, last_index_to_start + 1):
            if i[j] > best_digit:
                best_digit = i[j]
                best_position = j

        list_with_biggest_joltage.append(best_digit)
        start_index = best_position + 1
        remaining_digits_to_select -= 1

    num_to_add = int("".join(list_with_biggest_joltage))
    sum_pairs += num_to_add


print(sum_pairs)
