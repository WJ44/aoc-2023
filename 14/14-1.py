sum = 0
with open("./14/input.txt", "r", encoding="utf-8") as file:
    grid = [[c for c in line.rstrip()] for line in file]
    grid = [[row[i] for row in grid] for i in range(len(grid[0]))]
    for column in grid:
        free = 0
        for i in range(len(column)):
            if column[i] == ".":
                pass
            elif column[i] == "#":
                free = i + 1
            elif column[i] == "O":
                sum += len(column) - free
                if free == i:
                    free = i + 1
                else:
                    column[i] = "."
                    column[free] = "O"
                    free = min(free + 1, i)

print(sum)