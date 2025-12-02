import re

with open("input") as f:
    elements = f.read().strip().split("\n")

#elements = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"] #Example input


position = 50
count_zeros = 0

for el in elements:
    match = re.search(r"\d+", el)
    number = int(match.group())

    if el.startswith("L"):
        for _ in range(number):
            if position == 0:
                position = 100
            position = (position - 1)
            if position == 0:
                count_zeros += 1
                position = 100
        position = (position) % 100


    else:
        for _ in range(number):
            if position == 100:
                position = 0
            position = (position + 1)
            if position == 100:
                count_zeros += 1
                position = 0
        position = (position) % 100

print(count_zeros)