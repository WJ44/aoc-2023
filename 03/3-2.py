import re

solution = 0
gears = {}


def process_gear(gear):
    if gear in gears:
        gears[gear].append(int(match.group()))
    else:
        gears[gear] = [int(match.group())]


with open("./03/input.txt", "r", encoding="utf-8") as file:
    grid = [line.rstrip() for line in file]
    for i, line in enumerate(grid):
        for match in re.finditer(r"(\d)+", line):
            start, end = match.span()
            if start - 1 >= 0 and grid[i][start - 1] == "*":
                process_gear((i, start - 1))
            elif end < len(line) and grid[i][end] == "*":
                process_gear((i, end))
            else:
                start = max(0, start - 1)
                end = min(len(line), end + 1)
                for j in range(start, end):
                    if i - 1 >= 0 and grid[i - 1][j] == "*":
                        process_gear((i - 1, j))
                    elif i + 1 < len(grid) and grid[i + 1][j] == "*":
                        process_gear((i + 1, j))

for g in gears.values():
    if len(g) == 2:
        solution += g[0] * g[1]

print(solution)
