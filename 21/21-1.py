start = (0, 0)
rocks = set()

with open("./21/input.txt", "r") as file:
    grid = [[c for c in line.rstrip()] for line in file]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                rocks.add((x, y))
            elif grid[y][x] == "S":
                start = (x, y)

plots = {start}
for i in range(64):
    new_plots = set()
    for x, y in plots:
        north = (x, y-1)
        west = (x+1, y)
        south = (x, y+1)
        east = (x-1, y)
        if north not in rocks:
            new_plots.add(north)
        if west not in rocks:
            new_plots.add(west)
        if south not in rocks:
            new_plots.add(south)
        if east not in rocks:
            new_plots.add(east)
    plots = new_plots

print(len(plots))