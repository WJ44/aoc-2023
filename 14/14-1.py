total = 0
with open("./14/input.txt", "r", encoding="utf-8") as file:
    grid = [list(line.rstrip()) for line in file]
    grid = [[row[i] for row in grid] for i in range(len(grid[0]))]
    for column in grid:
        free = 0
        for i, item in enumerate(column):
            if item == ".":
                pass
            elif item == "#":
                free = i + 1
            elif item == "O":
                total += len(column) - free
                if free == i:
                    free = i + 1
                else:
                    column[i] = "."
                    column[free] = "O"
                    free = min(free + 1, i)

print(total)
