import re

seeds = []

with open("./05/input.txt", "r", encoding="utf-8") as file:
    source = ""
    destination = ""
    for line in file:
        if m := re.match(r"(\d+) (\d+) (\d+)", line):
            destination_start = int(m.group(1))
            source_start = int(m.group(2))
            source_end = source_start + int(m.group(3))
            to_process = seeds.copy()
            seeds = []
            while to_process:
                seed = to_process.pop()
                length = seed["length"]
                if not(seed[source] + seed["length"] <= source_start or seed[source] >= source_end):
                    if seed[source] >= source_start and seed[source] + length <= source_end:
                        seed[destination] = destination_start + (seed[source] - source_start)
                        seeds.append(seed)
                    else:
                        copy = seed.copy()
                        new_source = source_end if seed[source] >= source_start else source_start
                        copy[source] = new_source
                        copy[destination] = new_source
                        seed["length"] = new_source - seed[source]
                        copy["length"] = copy["length"] - seed["length"]
                        to_process.extend([seed, copy])
                else:
                    seeds.append(seed)
        elif m := re.match(r"([a-z]+)-to-([a-z]+) map:", line):
            source = m.group(1)
            destination = m.group(2)
            for seed in seeds:
                seed[destination] = seed[source]
        elif m := re.match(r"seeds:([\s\d]+)", line):
            for string in re.findall(r"([\d]+ [\d]+)+", m.group(1)):
                start, length = string.split()
                seeds.append({"seed": int(start), "length": int(length)})

minimum = -1
for seed in seeds:
    minimum = seed["location"] if seed["location"] < minimum or minimum == -1 else minimum

print(minimum)
