from time import sleep

to_explore = set()

paths = [".", ">", "v", "<", "^"]

def print_path(grid, path):
    grid = grid.copy()
    for x, y in path:
        grid[y][x] = "O"
    for row in grid:
        print("".join(row))

from time import time

start_time = time()

max_distance = 0
with open("./23/input.txt", "r") as file:
    grid = [[c for c in line.rstrip()] for line in file]
    for x, cell in enumerate(grid[0]):
        if cell == ".":
            start = (x, 0, 0, 1)
            break
    for x, cell in enumerate(grid[-1]):
        if cell == ".":
            end = (x, len(grid)-1)
            break
    splits = {(start, -1, ())}
    while splits:
        # print(len(splits))
        node, distance, visited = splits.pop()
        to_explore = {node}
        visited = set(visited)
        visited.add((node[0], node[1]))
        while to_explore:
            distance += 1
            x, y, dx, dy = to_explore.pop()
            if (x, y) == end:
                max_distance = max(distance, max_distance)
                print(max_distance)
                continue
            neighbours = set()
            neighbour = (x + dx, y + dy)
            if neighbour not in visited and grid[y + dy][x + dx] in paths:
                neighbours.add((neighbour[0], neighbour[1], dx, dy))
            neighbour = (x + dy, y + -dx)
            if neighbour not in visited and grid[y + -dx][x + dy] in paths:
                neighbours.add((neighbour[0], neighbour[1], dy, -dx))
            neighbour = (x + -dy, y + dx)
            if neighbour not in visited and grid[y + dx][x + -dy] in paths:
                neighbours.add((neighbour[0], neighbour[1], -dy, dx))
            if len(neighbours) > 1:
                for neighbour in neighbours:
                    if not splits or all([other != neighbour or distance >= other_dist or (visited - set(other_visited) and not set(other_visited).issubset(visited)) for other, other_dist, other_visited in splits]):
                        splits.add((neighbour, distance, tuple(visited)))
            else:
                to_explore.update(neighbours)

print(time() - start_time)