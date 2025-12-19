from pathlib import Path
from typing import List




INPUT_PATH_RANGES = Path("./input_ranges.txt")
INPUT_PATH_INGREDIENTS_ID = Path("./input_ingredients_id.txt")

input_list_ranges: List[str] = []
input_list_ingredients_id: List[str] = []
count_fresh_id: int = 0


with open(INPUT_PATH_RANGES) as file:
    for line in file:
        input_list_ranges.append(line.strip())

with open(INPUT_PATH_INGREDIENTS_ID) as file:
    for line in file:
        input_list_ingredients_id.append(line.strip())


parsed_ranges: list[tuple[int, int]] = [(int(start), int(end)) for start, end in (r.split("-") for r in input_list_ranges)]

for id in input_list_ingredients_id:
    found: bool = False
    for ranges in parsed_ranges:
        if ranges[0]<= int(id) <= ranges[1]:
            found = True
            break
    if found:
        count_fresh_id += 1


print(count_fresh_id)