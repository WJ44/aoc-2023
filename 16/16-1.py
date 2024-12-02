seen = []
grid = []


def split(x, y, dx, dy):
    while not (y < 0 or y >= len(grid)) and not (x < 0 or x >= len(grid[y])):
        if (x, y, dx, dy) in seen:
            return
        seen.append((x, y, dx, dy))
        visited.add((x, y))
        if grid[y][x] == ".":
            x += dx
            y += dy
        elif grid[y][x] == "|":
            if dx:
                split(x, y + 1, 0, 1)
                split(x, y - 1, 0, -1)
            else:
                y += dy
        elif grid[y][x] == "-":
            if dy:
                split(x + 1, y, 1, 0)
                split(x - 1, y, -1, 0)
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
with open("./16/input.txt", "r", encoding="utf-8") as file:
    grid = [list(line.rstrip()) for line in file]
    split(0, 0, 1, 0)

print(len(visited))
