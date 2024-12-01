import re

directions = ""
network = {}

with open("./08/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        if m := re.match(r"(\w+) = \((\w+), (\w+)\)", line):
            network[m.group(1)] = {
                "L": m.group(2),
                "R": m.group(3)
            }
        elif m:= re.match(r"\w+", line):
            directions = m.group()

steps = 0
node = "AAA"
while node != "ZZZ":
    node = network[node][directions[steps % len(directions)]]
    steps += 1

print(steps)
