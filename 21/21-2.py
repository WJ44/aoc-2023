start = (0, 0)
rocks = set()
width = 0
height = 0

with open("./21/input.txt", "r", encoding="utf-8") as file:
    grid = [list(line.rstrip()) for line in file]
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if item == "#":
                rocks.add((x, y))
            elif item == "S":
                start = (x, y)
    width = len(grid[0])
    height = len(grid)

frontier = {start}
last = []
count = 1
last_count = 0
for i in range(1000):
    neighbours = set()
    for x, y in frontier:
        neighbours.add((x, y - 1))
        neighbours.add((x + 1, y))
        neighbours.add((x, y + 1))
        neighbours.add((x - 1, y))
    new_plots = set()
    for x, y in neighbours:
        if (x, y) in last:
            continue
        if (x % width, y % height) not in rocks:
            new_plots.add((x, y))
    last = frontier
    frontier = new_plots
    new_count = last_count
    last_count = count
    count = new_count + len(frontier)
    print(count)

# Analytically found a recursive function which is calculated below

intervals = [288, 177, 287, 163, 286, 182, 283, 194, 270, 190, 275, 205, 264, 217, 240, 228, 235, 240, 218, 240, 214, 232, 224, 228, 242, 215, 242, 222, 236, 228, 233, 245, 217, 262, 210, 271, 194, 266, 195, 279, 182, 288, 170, 282, 170, 282, 187, 288, 176, 278, 180, 288, 191, 290, 180, 287, 152, 316, 132, 320, 143, 321, 149, 307, 152, 317, 159, 313, 154, 314, 144, 311, 158, 291, 169, 296, 162, 301, 158, 307, 161, 289, 182, 289, 185, 305, 218, 315, 218, 308, 216, 308, 182, 276, 187, 291, 157, 293, 164, 305, 165, 291, 179, 292, 164, 303, 151, 317, 147, 318, 158, 312, 154, 308, 149, 313, 140, 330, 128, 316, 145, 300, 175, 292, 183, 288, 183, 282, 173, 276, 189]
current = 223572
previous_differences = [810, 504, 814, 468, 814, 524, 811, 565, 780, 548, 802, 591, 777, 630, 705, 671, 695, 709, 646, 714, 638, 693, 671, 685, 729, 649, 732, 673, 720, 694, 712, 750, 670, 802, 654, 833, 606, 828, 604, 871, 568, 909, 534, 893, 536, 896, 596, 920, 555, 896, 571, 928, 613, 941, 582, 932, 497, 1029, 428, 1047, 470, 1051, 493, 1017, 511, 1050, 537, 1037, 526, 1038, 498, 1024, 556, 960, 597, 979, 573, 1008, 553, 1041, 568, 981, 641, 984, 659, 1062, 764, 1097, 762, 1080, 760, 1084, 628, 989, 652, 1048, 545, 1059, 578, 1114, 572, 1071, 623, 1080, 569, 1125, 531, 1173, 523, 1176, 571, 1150, 562, 1139, 549, 1164, 520, 1231, 481, 1181, 543, 1126, 657, 1096, 696, 1086, 701, 1065, 665, 1046, 723]
start = 500
for i in range(start, 26501365):
    interval = intervals[(i - start) % len(intervals)]
    current += previous_differences[(i - start) % len(previous_differences)] + interval
    previous_differences[(i - start) % len(previous_differences)] += interval
print(current)
