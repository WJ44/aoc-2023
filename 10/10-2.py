connections_map = {
    (-1, 0): ["|", "F", "7", "S"],
    (0, -1): ["-", "F", "L", "S"],
    (0, 1): ["-", "7", "J", "S"],
    (1, 0): ["|", "L", "J", "S"]
}

def new_direction(direction, pipe):
    if pipe == "J" or pipe == "F":
        return (-direction[1], -direction[0])
    elif pipe == "L" or pipe == "7":
        return (direction[1], direction[0])
    else:
        return direction

with open("./10/input.txt", "r") as file:
    grid = [[c for c in line.rstrip()] for line in file]
    clean_grid = [["." for c in range(len(grid[r]))] for r in range(len(grid))]

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == "S":
                possible = []
                for offset, connections in connections_map.items():
                    r = row + offset[0]
                    c = column + offset[1]
                    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[row]):
                        if grid[r][c] in connections and grid[row][column] in connections_map[(-offset[0], -offset[1])]:
                            if not possible:
                                possible.extend(connections_map[(-offset[0], -offset[1])])
                                possible.remove("S")
                            else:
                                pipe = (set(possible) & set(connections_map[(-offset[0], -offset[1])])).pop()
                                grid[row][column] = (set(possible) & set(connections_map[(-offset[0], -offset[1])])).pop()
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
    for r in range(len(clean_grid)):
        for c in range(len(clean_grid[r])):
            if clean_grid[r][c] == "F":
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
                        for offset in connections_map.keys():
                            fronts.append((front[0] + offset[0], front[1] + offset[1]))
        position = (position[0] + direction[0], position[1] + direction[1])

    print(count)