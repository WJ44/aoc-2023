import re
from math import lcm

directions = ""
network = {}
start_nodes = []
end_nodes = []

with open("./08/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        if m := re.match(r"(\w+) = \((\w+), (\w+)\)", line):
            network[m.group(1)] = {"L": m.group(2), "R": m.group(3)}
            if re.match(r"\w+A", m.group(1)):
                start_nodes.append(m.group(1))
            elif re.match(r"\w+Z", m.group(1)):
                end_nodes.append(m.group(1))
        elif m := re.match(r"\w+", line):
            directions = m.group()

steps = 0
intervals = [-1] * len(start_nodes)
nodes = start_nodes.copy()
while -1 in intervals:
    for i, node in enumerate(nodes):
        nodes[i] = network[node][directions[steps % len(directions)]]
        if nodes[i][2] == "Z":
            if intervals[i] == -1:
                intervals[i] = steps + 1
    steps += 1

print(lcm(*intervals))
