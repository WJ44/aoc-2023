import re

maximum = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum = 0

with open("./2/input.txt", "r") as file:
    for line in file:
        m = re.match(r"Game (?P<id>\d+):(?P<game>.*)", line)
        id = int(m['id'])
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
            sum += id

print(sum)