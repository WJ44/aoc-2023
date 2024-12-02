import re

seeds = {}

with open("./05/input.txt", "r", encoding="utf-8") as file:
    source = ""
    destination = ""
    for line in file:
        if m := re.match(r"(\d+) (\d+) (\d+)", line):
            destination_start = int(m.group(1))
            source_start = int(m.group(2))
            length = int(m.group(3))
            source_range = range(source_start, source_start + length)
            destination_range = range(destination_start, destination_start + length)
            for seed in seeds.values():
                if seed[source] in source_range:
                    seed[destination] = destination_start + (seed[source] - source_start)
        elif m := re.match(r"([a-z]+)-to-([a-z]+) map:", line):
            if source and destination:
                for seed in seeds.values():
                    if destination not in seed:
                        seed[destination] = seed[source]
            source = m.group(1)
            destination = m.group(2)
        elif m := re.match(r"seeds:([\s\d]+)", line):
            for string in m.group(1).split():
                seed = int(string)
                seeds[seed] = {"seed": seed}
    for seed in seeds.values():
        if destination not in seed:
            seed[destination] = seed[source]

minimum = -1
for seed in seeds.values():
    if minimum == -1:
        minimum = seed["location"]
    elif minimum > seed["location"]:
        minimum = seed["location"]

print(minimum)
