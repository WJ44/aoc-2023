import re

from tqdm import tqdm

direction_map = {
    "3": (0, -1),
    "0": (1, 0),
    "1": (0, 1),
    "2": (-1, 0)
}

x = 0
y = 0

instructions = []

with open("./18/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        distance, direction = re.match(r"[URDL] \d+ \(#(\w{5})(\w)\)", line).groups()
        distance = int(distance, 16)
        dx, dy = direction_map[direction]
        x += dx*(distance)
        y += dy*(distance)
        instructions.append((dx + dy)*distance)

area = 1
x = 0
for i in range(0, len(instructions), 2):
    x += instructions[i]
    area += x * instructions[i + 1]
    area += 0.5 * abs(instructions[i])
    area += 0.5 * abs(instructions[i+1])

print(area)