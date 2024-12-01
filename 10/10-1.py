connections_map = {
    (-1, 0): ["|", "F", "7", "S"],
    (0, -1): ["-", "F", "L", "S"],
    (0, 1): ["-", "7", "J", "S"],
    (1, 0): ["|", "L", "J", "S"],
}

with open("./10/input.txt", "r", encoding="utf-8") as file:
    grid = [list(line.rstrip()) for line in file]

    fronts = []
    for row, grid_row in enumerate(grid):
        for column, grid_item in enumerate(grid_row):
            if grid_item != ".":
                count = 0
                for offset, connections in connections_map.items():
                    r = row + offset[0]
                    c = column + offset[1]
                    if 0 <= r < len(grid) and 0 <= c < len(grid_row):
                        if (
                            grid[r][c] in connections
                            and grid_item
                            in connections_map[(-offset[0], -offset[1])]
                        ):
                            count += 1
                if count != 2:
                    fronts.append((row, column))
    while fronts:
        new_fronts = []
        for row, column in fronts:
            for offset, connections in connections_map.items():
                r = row + offset[0]
                c = column + offset[1]
                if 0 <= r < len(grid) and 0 <= c < len(grid[row]):
                    if (
                        grid[r][c] in connections
                        and grid[row][column]
                        in connections_map[(-offset[0], -offset[1])]
                    ):
                        new_fronts.append((r, c))
            grid[row][column] = "."
        fronts = new_fronts
    fronts = []
    for row, gird_row in enumerate(grid):
        for column, grid_item in enumerate(gird_row):
            if grid_item == "S":
                grid[row][column] = 0
                fronts.append((row, column))

    i = 0
    while fronts:
        new_fronts = []
        for row, column in fronts:
            if grid[row][column] == i:
                for offset, connections in connections_map.items():
                    r = row + offset[0]
                    c = column + offset[1]
                    if 0 <= r < len(grid) and 0 <= c < len(grid[row]):
                        if grid[r][c] in connections:
                            grid[r][c] = i + 1
                            new_fronts.append((r, c))
        fronts = new_fronts
        i += 1

print(i - 1)
