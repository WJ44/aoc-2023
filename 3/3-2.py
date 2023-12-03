import re

sum = 0
gears = {}

with open("./3/input.txt", "r") as file:
    grid = [line.rstrip() for line in file]
    for i, line in enumerate(grid):
        for match in re.finditer(r"(\d)+", line):
            start, end = match.span()
            if start - 1 >= 0 and grid[i][start - 1] == '*':
                gear = (i, start - 1)
                if gear in gears:
                    gears[gear].append(int(match.group()))
                else:
                    gears[gear] = [int(match.group())]
            elif end < len(line) and grid[i][end] == '*':
                gear = (i, end)
                if gear in gears:
                    gears[gear].append(int(match.group()))
                else:
                    gears[gear] = [int(match.group())]
            else:
                start = max(0, start - 1)
                end = min(len(line), end + 1)
                for j in range(start, end):
                    if i - 1 >= 0 and grid[i-1][j] == '*':
                        gear = (i-1, j)
                        if gear in gears:
                            gears[gear].append(int(match.group()))
                        else:
                            gears[gear] = [int(match.group())]
                    elif i + 1 < len(grid) and grid[i+1][j] == '*':
                        gear = (i+1, j)
                        if gear in gears:
                            gears[gear].append(int(match.group()))
                        else:
                            gears[gear] = [int(match.group())]

for gear in gears.values():
    if len(gear) == 2:
        sum += gear[0] * gear[1]

print(sum)