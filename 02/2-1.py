import re

maximum = {
    'red': 12,
    'green': 13,
    'blue': 14
}

solution = 0

with open("./02/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        m = re.match(r"Game (?P<id>\d+):(?P<game>.*)", line)
        identifier = int(m['id'])
        grabs = m['game'].split(";")
        impossible = False
        for grab in grabs:
            if impossible:
                break
            colors = re.findall(r"(\d+) ([a-z]+)", grab)
            for color in colors:
                if int(color[0]) > maximum[color[1]]:
                    impossible = True
                    break
        if not impossible:
            solution += identifier

print(solution)
