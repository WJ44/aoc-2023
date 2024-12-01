paths = [".", ">", "v", "<", "^"]

graph = {}
with open("./23/input.txt", "r", encoding="utf-8") as file:
    grid = [[c for c in line.rstrip()] for line in file]
    for x, cell in enumerate(grid[0]):
        if cell == ".":
            start = (x, 0)
            break
    for x, cell in enumerate(grid[-1]):
        if cell == ".":
            end = (x, len(grid)-1)
            break

    to_explore = {(start[0], start[1], 0, 1)}
    while to_explore:
        node = to_explore.pop()
        neighbours = {node}
        distance = 0
        while True:
            x, y, dx, dy = neighbours.pop()
            distance += 1
            if (x, y) == end:
                if (node[0] - node[2], node[1] - node[3]) in graph:
                    graph[(node[0] - node[2], node[1] - node[3])].add(((x, y), distance))
                else:
                    graph[(node[0] - node[2], node[1] - node[3])] = {((x, y), distance)}
                break
            if grid[y + dy][x + dx] in paths:
                neighbour = (x + dx, y + dy)
                neighbours.add((neighbour[0], neighbour[1], dx, dy))
            if grid[y + -dx][x + dy] in paths:
                neighbour = (x + dy, y + -dx)
                neighbours.add((neighbour[0], neighbour[1], dy, -dx))
            if grid[y + dx][x + -dy] in paths:
                neighbour = (x + -dy, y + dx)
                neighbours.add((neighbour[0], neighbour[1], -dy, dx))
            if len(neighbours) > 1:
                if (node[0] - node[2], node[1] - node[3]) in graph:
                    graph[(node[0] - node[2], node[1] - node[3])].add(((x, y), distance))
                else:
                    graph[(node[0] - node[2], node[1] - node[3])] = {((x, y), distance)}
                break
        for neighbour in neighbours:
            if (x, y) not in graph:
                to_explore.add(neighbour)

for node, neighbours in graph.items():
    for neighbour, distance in neighbours:
        if neighbour != end:
            graph[neighbour].add((node, distance))

def explore(node, path, distance):
    path = path.copy()
    if node == end:
        return distance
    path.append(node)
    max_distance = 0
    for neighbour, dist in graph[node]:
        if neighbour not in path:
            max_distance = max(max_distance, explore(neighbour, path, distance + dist))
    return max_distance

print(explore((start[0], start[1] - 1), [], -1))