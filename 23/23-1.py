from time import sleep

to_explore = set()
distance = {}

slopes = {
    (1, 0): ">",
    (0, 1): "v",
    (-1, 0): "<",
    (0, -1): "^"
}

with open("./23/input.txt", "r", encoding="utf-8") as file:
    grid = [[c for c in line.rstrip()] for line in file]
    for x, cell in enumerate(grid[0]):
        if cell == ".":
            start = (x, 0, 0, 1)
            break
    for x, cell in enumerate(grid[-1]):
        if cell == ".":
            end = (x, len(grid)-1)
            break
    distance[(start[0], start[1])] = 0
    to_explore.add(start)
    while to_explore:
        x, y, dx, dy = to_explore.pop()
        dist = distance[(x, y)]
        if (x, y) == end:
            continue
        new_dist = dist + 1
        if grid[y + dy][x + dx] == "." or grid[y + dy][x + dx] == slopes[(dx, dy)]:
            neighbour = (x + dx, y + dy)
            if not neighbour in distance or distance[neighbour] < new_dist:
                distance[neighbour] = new_dist
            to_explore.add((neighbour[0], neighbour[1], dx, dy))
        if grid[y + -dx][x + dy] == "." or grid[y + -dx][x + dy] == slopes[(dy, -dx)]:
            neighbour = (x + dy, y + -dx)
            if not neighbour in distance or distance[neighbour] < new_dist:
                distance[neighbour] = new_dist
            to_explore.add((neighbour[0], neighbour[1], dy, -dx))
        if grid[y + dx][x + -dy] == "." or grid[y + dx][x + -dy] == slopes[(-dy, dx)]:
            neighbour = (x + -dy, y + dx)
            if not neighbour in distance or distance[neighbour] < new_dist:
                distance[neighbour] = new_dist
            to_explore.add((neighbour[0], neighbour[1], -dy, dx))
    print(distance[end])