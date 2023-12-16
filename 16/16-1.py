import sys

seen = []
def split(x, y, dx, dy, grid, visited):
    while not (y < 0 or y >= len(grid)) and not (x < 0 or x >= len(grid[y])):
        if (x, y, dx, dy) in seen:
            return
        else:
            seen.append((x, y, dx, dy))
        visited.add((x, y))
        if grid[y][x] == ".":
            x += dx
            y += dy
        elif grid[y][x] == "|":
            if dx:
                split(x, y+1, 0, 1, grid, visited)
                split(x, y-1, 0, -1, grid, visited)
            else:
                y += dy
        elif grid[y][x] == "-":
            if dy:
                split(x+1, y, 1, 0, grid, visited)
                split(x-1, y, -1, 0, grid, visited)
            else:
                x += dx
        elif grid[y][x] == "\\":
            if dx:
                dy = dx
                dx = 0
                y += dy
            else:
                dx = dy
                dy = 0
                x += dx
        elif grid[y][x] == "/":
            if dx:
                dy = -dx
                dx = 0
                y += dy
            else:
                dx = -dy
                dy = 0
                x += dx

visited = set()
with open("./16/input.txt", "r") as file:
    grid = [[c for c in line.rstrip()] for line in file]
    split(0, 0, 1, 0, grid, visited)

print(len(visited))