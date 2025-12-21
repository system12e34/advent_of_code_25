from pathlib import Path
from typing import List, Any
from functools import reduce
from operator import mul



INPUT = Path("./input.txt")
input_list: List[str] = []
transpose_list: List[List[Any]] = []
operators: str = ""
sum_elements: int = 0
total_sum_elements: int = 0


with open(INPUT) as file:
    for line in file:
        input_list.append(line.split())


operators = input_list[-1]


transpose_list = [list(col) for col in zip(*input_list)]

for position, element in enumerate(transpose_list):
    digits = [int(x) for x in element if str(x).isdigit()]

    if operators[position] == "+":
        sum_elements = sum(digits)
    elif operators[position] == "*":
        sum_elements = reduce(mul, digits, 1)
    else:
        continue

    total_sum_elements += sum_elements

print(total_sum_elements)
