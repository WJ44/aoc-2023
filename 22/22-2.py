pile = set()
bricks = []
part_of_brick = {}
supported_by = {}
snapshot = []

with open("./22/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        coord1, coord2 = line.split("~")
        x1, y1, z1 = [int(i) for i in coord1.split(",")]
        x2, y2, z2 = [int(i) for i in coord2.split(",")]
        cubes = [[x, y, z] for x in range(x1, x2+1) for y in range(y1, y2+1) for z in range(z1, z2+1)]
        snapshot.append(sorted(cubes, key=lambda cube: cube[2]))

for brick in sorted(snapshot, key=lambda brick: brick[0][2]):
    supported_by_bricks = set()
    while not any(cube[2] == 1 for cube in brick):
        supported_by_cubes = [(cube[0], cube[1], cube[2]-1) for cube in brick if (cube[0], cube[1], cube[2]-1) in pile]
        if supported_by_cubes:
            for cube in supported_by_cubes:
                cube = tuple(cube)
                supported_by_bricks.add(part_of_brick[cube])
            break
        for cube in brick:
            cube[2] -= 1
    cubes = tuple(tuple(cube) for cube in brick)
    for cube in cubes:
        part_of_brick[cube] = cubes
    supported_by[cubes] = supported_by_bricks
    pile.update(cubes)
    bricks.append(cubes)

def find_falling(falling, fallen):
    if not falling:
        return 0
    new_falling = set()
    supports = set()
    for brick in falling:
        for cube in brick:
            if (cube[0], cube[1], cube[2]+1) in part_of_brick:
                supports.add(part_of_brick[(cube[0], cube[1], cube[2]+1)])
    for brick in supports:
        if not brick in falling and not supported_by[brick] - falling - fallen:
            new_falling.add(brick)
    fallen.update(falling)
    return len(new_falling) + find_falling(new_falling, fallen)

count = 0
for brick in bricks:
    count += find_falling({brick}, set())

print(count)