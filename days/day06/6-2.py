from pathlib import Path
from typing import List, Any
from functools import reduce
from operator import mul



INPUT = Path("./input.txt")
op_line: str
operators: str = ""
col_starts: List[int] = []
matrix: List[List[Any]] = []
transposed: List[List[Any]] = []
len_elements: int = 0
sum_elements: int = 0
total_sum_elements: int = 0



with INPUT.open() as f:
    lines = [line.rstrip("\n") for line in f if line.strip()]

op_line = lines[-1]
operators = op_line.split()

col_starts = [i for i, ch in enumerate(op_line) if ch in "+*"]

def slice_by_columns(line, starts):
    groups: List[str] = []
    for i, start in enumerate(starts):
        if i + 1 < len(starts):
            end = starts[i + 1] - 1   # skip separator space
        else:
            end = len(line)
        groups.append(line[start:end])
    return groups


for line in lines:
    if not line.startswith(("*","+")):
        groups = slice_by_columns(line, col_starts)
        groups = [g.replace(" ", "-") for g in groups]
        matrix.append(groups)


transposed = [list(col) for col in zip(*matrix)]


for position, element in enumerate(transposed):
    len_elements = len(element[0])
    list_elements = []
    for i in range(len_elements):
        sum_elements = 0
        s = int("".join(
            ch if ch.isdigit() else ""
            for ch in (
                element[0][-i - 1],
                element[1][-i - 1],
                element[2][-i - 1],
                element[3][-i - 1],
            )
        ))
        digit_s = int(s) if s else 0
        list_elements.append(digit_s)

    if operators[position] == "+":
        sum_elements = sum(list_elements)
    elif operators[position] == "*":
        sum_elements= reduce(mul, list_elements, 1)
    else:
        continue

    total_sum_elements += sum_elements


print(total_sum_elements)

