import re

solution = 0

with open("./03/input.txt", "r", encoding="utf-8") as file:
    grid = [line.rstrip() for line in file]
    for i, line in enumerate(grid):
        for match in re.finditer(r"(\d)+", line):
            start, end = match.span()
            if start - 1 >= 0 and grid[i][start - 1] != '.' and not grid[i][start - 1].isdigit():
                solution += int(match.group())
            elif end < len(line) and grid[i][end] != '.' and not grid[i][end].isdigit():
                solution += int(match.group())
            else:
                start = max(0, start - 1)
                end = min(len(line), end + 1)
                for j in range(start, end):
                    if i - 1 >= 0 and grid[i-1][j] != '.' and not grid[i-1][j].isdigit():
                        solution += int(match.group())
                        break
                    elif i + 1 < len(grid) and grid[i+1][j] != '.' and not grid[i+1][j].isdigit():
                        solution += int(match.group())
                        break

print(solution)
