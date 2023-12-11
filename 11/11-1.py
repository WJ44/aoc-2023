galaxies = []

with open("./11/input.txt", "r") as file:
    grid = [[c for c in line.rstrip()] for line in file]
    i = 0
    while i < len(grid):
        row = grid[i]
        if all([c == "." for c in row]):
            grid.insert(i, row.copy())
            i += 1
        i += 1
    i = 0
    while i < len(grid[0]):
        column = [row[i] for row in grid]
        if all([c == "." for c in column]):
            for row in grid:
                row.insert(i, ".")
            i += 1
        i += 1
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == "#":
                galaxies.append((row, column))

sum = 0
for distance in [abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) if g1 != g2 else 0 for g1 in galaxies for g2 in galaxies]:
    sum += distance

print(sum // 2)