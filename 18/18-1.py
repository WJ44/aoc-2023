import re

direction_map = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
max_x = 0
max_y = 0
min_y = 0
min_x = 0

x = 0
y = 0

instructions = []

with open("./18/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        direction, distance, color = re.match(r"([URDL]) (\d+) \(#(\w+)\)", line).groups()
        distance = int(distance)
        dx, dy = direction_map[direction]
        x += dx * (distance)
        y += dy * (distance)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        instructions.append((dx, dy, distance, color))

grid = [["."] * (max_x + 1 - min_x) for _ in range(max_y + 1 - min_y)]
x = -min_x
y = -min_y

grid[y][x] = "#"
for dx, dy, distance, color in instructions:
    if dx:
        for i in range(x + dx, x + dx * distance + dx, dx):
            x = i
            grid[y][x] = "#"
    if dy:
        for i in range(y + dy, y + dy * distance + dy, dy):
            y = i
            grid[i][x] = "#"

count = 0
for y, row in enumerate(grid):
    previous = False
    line = False
    inside = False
    for x, item in enumerate(row):
        if item == "#":
            count += 1
            if previous:
                line = True
            if not line:
                inside = not inside
                previous = True
        else:
            previous = False
            if line:
                if y == 0 or grid[y - 1][x] != "#":
                    inside = False
                else:
                    inside = True
                line = False
            if inside:
                grid[y][x] = "#"
                count += 1

print(count)
