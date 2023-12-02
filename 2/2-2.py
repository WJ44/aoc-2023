import re

sum = 0

with open("./2/input.txt", "r") as file:
    for line in file:
        cubes = {
            'red': None,
            'green': None,
            'blue': None
        }
        m = re.match(r"Game (?P<id>\d+):(?P<game>.*)", line)
        id = int(m['id'])
        grabs = m['game'].split(";")
        for grab in grabs:
            colors = re.findall(r"(\d+) ([a-z]+)", grab)
            for color in colors:
                name = color[1]
                amount = int(color[0])
                if cubes[name] and cubes[name] >= amount:
                    continue
                cubes[name] = amount
        power = 1
        for color in cubes.values():
            if color:
                power *= color
        sum += power

print(sum)
