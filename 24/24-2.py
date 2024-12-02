from itertools import combinations

equations = []

with open("./24/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        position, velocity = line.split(" @ ")
        px, py, pz = position.split(", ")
        vx, vy, vz = velocity.split(", ")
        a = int(vy) / int(vx)
        b = -a * int(px) + int(py)
        equations.append((a, b, int(px), int(vx)))

count = 0
for (a, b, px1, vx1), (c, d, px2, vx2) in combinations(equations, 2):
    if a != c:
        x = (d - b) / (a - c)
        y = a * x + b
        if (
            (x - px1) / vx1 > 0
            and (x - px2) / vx2 > 0
            and 400000000000000 >= x >= 200000000000000
            and 400000000000000 >= y >= 200000000000000
        ):
            count += 1

print(count)
