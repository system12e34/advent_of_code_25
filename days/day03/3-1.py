from pathlib import Path
from typing import List

INPUT_PATH = Path("./input.txt")

input_list:List[str] = []
sum_pairs:int = 0


with open(INPUT_PATH) as file:
    for line in file:
        input_list.append(line.strip())


def find_pair_max_digits(input_elements: str) -> List[str]:
    """
    Find 2 max digits in the list.
    Where the second digit goes after the first digit
    """
    first_max_digit = max(input_elements[:-1])
    index_first_max_digit = input_elements.index(first_max_digit)
    second_max_digit = max(input_elements[index_first_max_digit+1:])

    return [first_max_digit, second_max_digit]


for line in input_list:
    first_max_digit,second_max_digit = find_pair_max_digits(line)
    concat_pair = f"{first_max_digit}{second_max_digit}"
    sum_pairs += int(concat_pair)


print(sum_pairs)
