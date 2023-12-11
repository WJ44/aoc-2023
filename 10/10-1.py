connections_map = {
    (-1, 0): ["|", "F", "7", "S"],
    (0, -1): ["-", "F", "L", "S"],
    (0, 1): ["-", "7", "J", "S"],
    (1, 0): ["|", "L", "J", "S"]
}

with open("./10/input.txt", "r") as file:
    grid = [[c for c in line.rstrip()] for line in file]

    fronts = []
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] != ".":
                count = 0
                for offset, connections in connections_map.items():
                    r = row + offset[0]
                    c = column + offset[1]
                    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[row]):
                        if grid[r][c] in connections and grid[row][column] in connections_map[(-offset[0], -offset[1])]:
                            count += 1
                if count != 2:
                    fronts.append((row, column))   
    
    while fronts:
        new_fronts = []
        for row, column in fronts:
            for offset, connections in connections_map.items():
                r = row + offset[0]
                c = column + offset[1]
                if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[row]):
                    if grid[r][c] in connections and grid[row][column] in connections_map[(-offset[0], -offset[1])]:
                        new_fronts.append((r, c))
            grid[row][column] = "."
        fronts = new_fronts
    
    fronts = []
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == "S":
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
                    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[row]):
                        if grid[r][c] in connections:
                            grid[r][c] = i + 1
                            new_fronts.append((r, c))
        fronts = new_fronts
        i += 1

print(i-1)