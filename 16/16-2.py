import sys

def split(x, y, dx, dy, grid, visited, seen):
    while not (y < 0 or y >= len(grid)) and not (x < 0 or x >= len(grid[y])):
        if (x, y, dx, dy) in seen:
            return
        else:
            seen.add((x, y, dx, dy))
        visited.add((x, y))
        if grid[y][x] == ".":
            x += dx
            y += dy
        elif grid[y][x] == "|":
            if dx:
                split(x, y+1, 0, 1, grid, visited, seen)
                split(x, y-1, 0, -1, grid, visited, seen)
            else:
                y += dy
        elif grid[y][x] == "-":
            if dy:
                split(x+1, y, 1, 0, grid, visited, seen)
                split(x-1, y, -1, 0, grid, visited, seen)
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

def start_count(x, y, dx, dy, grid):
    seen = set()
    visited = set()
    split(x, y, dx, dy, grid, visited, seen)
    return len(visited)

maximum = 0
with open("./16/input.txt", "r") as file:
    grid = [[c for c in line.rstrip()] for line in file]
    for y in range(len(grid)):
        maximum = max(maximum, start_count(0, y, 1, 0, grid))
        maximum = max(maximum, start_count(len(grid[y]) - 1, y, -1, 0, grid))
    for x in range(len(grid[y])):
        maximum = max(maximum, start_count(x, 0, 0, 1, grid))
        maximum = max(maximum, start_count(x, len(grid), 0, -1, grid))

print(maximum)