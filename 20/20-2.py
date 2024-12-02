import re
from collections import deque
from math import lcm

modules = {}
states = {}
with open("./20/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        kind, name, destinations = re.match(r"([%&]?)([a-z]+) -> (.*)", line).groups()
        destinations = destinations.split(", ")
        modules[name] = (kind, destinations)
        if kind == "%":
            states[name] = -1
        elif kind == "&":
            states[name] = {}

for name, (_, destinations) in modules.items():
    for destination in destinations:
        if destination in modules and modules[destination][0] == "&":
            states[destination][name] = -1

periods = {}
stack = deque()
i = 1
found = False
while not found:
    stack.append(("broadcaster", -1, "button"))
    while stack:
        name, pulse, source = stack.popleft()
        if name == "nc" and pulse == 1:
            if source not in periods:
                periods[source] = i
            if all(module in periods for module in states[name].keys()):
                found = True
                break
        if name not in modules:
            continue
        kind, destinations = modules[name]
        send = True
        if kind == "%":
            if pulse == -1:
                states[name] *= pulse
                pulse = states[name]
            else:
                send = False
        elif kind == "&":
            states[name][source] = pulse
            pulse = -1 if sum(states[name].values()) == len(states[name].values()) else 1
        if send:
            stack.extend((module, pulse, name) for module in destinations)
    i += 1

print(lcm(*periods.values()))
