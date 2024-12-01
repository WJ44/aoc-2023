from heapq import heappop, heappush

to_explore_entries = {}
to_explore = []
g = {}

def h(node, x_goal, y_goal):
    return x_goal - node[0] + y_goal - node[1]

def explore(current, dx, dy, straight):
    neighbour = (current[0] + dx, current[1] + dy, dx, dy, straight)
    if neighbour[0] >= 0 and neighbour[0] <= x_goal and neighbour[1] >= 0 and neighbour[1] <= y_goal:
        new_g = g[current] + grid[neighbour[1]][neighbour[0]]
        if neighbour not in g or new_g < g[neighbour]:
            g[neighbour] = new_g
            if neighbour in to_explore_entries:
                entry = to_explore_entries.pop(neighbour)
                entry[1] = None
            entry = (new_g + h(neighbour, x_goal, y_goal), neighbour)
            to_explore_entries[neighbour] = entry
            heappush(to_explore, entry)


with open("./17/input.txt", "r", encoding="utf-8") as file:
    grid = [[int(c) for c in line.rstrip()] for line in file]
    x_goal = len(grid[0]) - 1
    y_goal = len(grid) - 1
    #x, y, dx, dy, straight
    start = (0, 0, 1, 0, 0)
    entry = (h(start, x_goal, y_goal), start)
    to_explore_entries[start] = entry
    heappush(to_explore, entry)
    g[start] = 0
    while to_explore:
        current = None
        while not current:
            current = heappop(to_explore)[1]
        del to_explore_entries[current]
        if current[0] == x_goal and current[1] == y_goal:
            print(g[current])
            break
        if current[4] < 3:
            explore(current, current[2], current[3], current[4] + 1)
        explore(current, -current[3], current[2], 1)
        explore(current, current[3], -current[2], 1)