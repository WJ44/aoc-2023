connections_map = {
    (-1, 0): ["|", "F", "7", "S"],
    (0, -1): ["-", "F", "L", "S"],
    (0, 1): ["-", "7", "J", "S"],
    (1, 0): ["|", "L", "J", "S"],
}


def new_direction(d, p):
    if p in ["J", "F"]:
        return (-d[1], -d[0])
    if p in ["L", "7"]:
        return (d[1], d[0])
    return d


with open("./10/input.txt", "r", encoding="utf-8") as file:
    grid = [list(line.rstrip()) for line in file]
    clean_grid = [["." for c in range(len(grid[r]))] for r in range(len(grid))]

    start = (-1, -1)
    for row, grid_row in enumerate(grid):
        for column, grid_item in enumerate(grid_row):
            if grid_item == "S":
                possible = []
                for offset, connections in connections_map.items():
                    r = row + offset[0]
                    c = column + offset[1]
                    if 0 <= r < len(grid) and 0 <= c < len(grid_row):
                        if grid[r][c] in connections and grid_item in connections_map[(-offset[0], -offset[1])]:
                            if not possible:
                                possible.extend(connections_map[(-offset[0], -offset[1])])
                                possible.remove("S")
                            else:
                                pipe = (set(possible) & set(connections_map[(-offset[0], -offset[1])])).pop()
                                grid[row][column] = (
                                    set(possible) & set(connections_map[(-offset[0], -offset[1])])
                                ).pop()
                                start = (row, column)
                                clean_grid[row][column] = pipe

    if pipe in ["F", "-", "L"]:
        direction = (0, 1)
    elif pipe in ["|", "7"]:
        direction = (1, 0)
    else:
        direction = (-1, 0)

    position = (start[0] + direction[0], start[1] + direction[1])
    while position != start:
        pipe = grid[position[0]][position[1]]
        clean_grid[position[0]][position[1]] = pipe
        direction = new_direction(direction, pipe)
        position = (position[0] + direction[0], position[1] + direction[1])

    start = None
    for r, clean_grid_r in enumerate(clean_grid):
        for c, clean_grid_item in enumerate(clean_grid_r):
            if clean_grid_item == "F":
                start = (r, c)
                break
        if start:
            break

    direction = (0, 1)
    position = (start[0] + direction[0], start[1] + direction[1])
    count = 0
    while position != start:
        insides = [(direction[1], -direction[0])]
        pipe = clean_grid[position[0]][position[1]]
        direction = new_direction(direction, pipe)
        insides.append((direction[1], -direction[0]))
        for inside in insides:
            neighbour = clean_grid[position[0] + inside[0]][position[1] + inside[1]]
            if neighbour == ".":
                fronts = []
                fronts.append((position[0] + inside[0], position[1] + inside[1]))
                while fronts:
                    front = fronts.pop()
                    if clean_grid[front[0]][front[1]] == ".":
                        clean_grid[front[0]][front[1]] = "I"
                        count += 1
                        for offset in connections_map:
                            fronts.append((front[0] + offset[0], front[1] + offset[1]))
        position = (position[0] + direction[0], position[1] + direction[1])

    print(count)
