def split(x, y, dx, dy, current_visited, seen):
    while not (y < 0 or y >= len(grid)) and not (x < 0 or x >= len(grid[y])):
        if (x, y, dx, dy) in seen:
            return
        seen.add((x, y, dx, dy))
        current_visited.add((x, y))
        if grid[y][x] == ".":
            x += dx
            y += dy
        elif grid[y][x] == "|":
            if dx:
                split(x, y + 1, 0, 1, current_visited, seen)
                split(x, y - 1, 0, -1, current_visited, seen)
            else:
                y += dy
        elif grid[y][x] == "-":
            if dy:
                split(x + 1, y, 1, 0, current_visited, seen)
                split(x - 1, y, -1, 0, current_visited, seen)
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


def start_count(x, y, dx, dy):
    seen_start = set()
    visited = set()
    split(x, y, dx, dy, visited, seen_start)
    return len(visited)


maximum = 0
grid = []
with open("./16/input.txt", "r", encoding="utf-8") as file:
    grid = [list(line.rstrip()) for line in file]
    for r, row in enumerate(grid):
        maximum = max(maximum, start_count(0, r, 1, 0))
        maximum = max(maximum, start_count(len(row) - 1, r, -1, 0))
    for c, _ in enumerate(grid[0]):
        maximum = max(maximum, start_count(c, 0, 0, 1))
        maximum = max(maximum, start_count(c, len(grid), 0, -1))

print(maximum)
