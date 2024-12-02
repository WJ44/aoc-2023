galaxies = []

with open("./11/input.txt", "r", encoding="utf-8") as file:
    grid = [list(line.rstrip()) for line in file]
    i = 0
    while i < len(grid):
        row = grid[i]
        if all(c == "." for c in row):
            grid[i] = len(row) * [":"]
            i += 1
        i += 1
    i = 0
    while i < len(grid[0]):
        column = [row[i] for row in grid]
        if all(c in [".", ":"] for c in column):
            for row in grid:
                row[i] = ":"
            i += 1
        i += 1
    for row, grid_row in enumerate(grid):
        for column, grid_item in enumerate(grid_row):
            if grid_item == "#":
                galaxies.append((row, column))

total = 0
for g1 in galaxies:
    for g2 in galaxies:
        distance = 0
        for i in range(min(g1[0], g2[0]), max(g1[0], g2[0])):
            if grid[i][0] == ":":
                distance += 999999
            distance += 1
        for i in range(min(g1[1], g2[1]), max(g1[1], g2[1])):
            if grid[0][i] == ":":
                distance += 999999
            distance += 1
        total += distance

print(total // 2)
