from pathlib import Path
from typing import List




INPUT_PATH_RANGES = Path("./input_ranges.txt")

input_list_ranges: List[str] = []
total_ranges: list = []
sum_ids: int = 0


with open(INPUT_PATH_RANGES) as file:
    for line in file:
        input_list_ranges.append(line.strip())


parsed_ranges: list[tuple[int, int]] = [(int(start), int(end)) for start, end in (r.split("-") for r in input_list_ranges)]

parsed_ranges = sorted(parsed_ranges)


for start, end in parsed_ranges:
    if not total_ranges:
        total_ranges.append([start, end])
        continue

    last_start, last_end = total_ranges[-1]

    if start <= last_end:
        total_ranges[-1][1] = max(last_end, end)
    else:
        total_ranges.append([start, end])

for start, end in total_ranges:
    sum_ids += (end+1) - start

print(sum_ids)
