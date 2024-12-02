galaxies = []

with open("./11/input.txt", "r", encoding="utf-8") as file:
    grid = [list(line.rstrip()) for line in file]
    i = 0
    while i < len(grid):
        row = grid[i]
        if all(c == "." for c in row):
            grid.insert(i, row.copy())
            i += 1
        i += 1
    i = 0
    while i < len(grid[0]):
        column = [row[i] for row in grid]
        if all(c == "." for c in column):
            for row in grid:
                row.insert(i, ".")
            i += 1
        i += 1
    for row, grid_row in enumerate(grid):
        for column, grid_item in enumerate(grid_row):
            if grid_item == "#":
                galaxies.append((row, column))

total = 0
for distance in [abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) if g1 != g2 else 0 for g1 in galaxies for g2 in galaxies]:
    total += distance

print(total // 2)
