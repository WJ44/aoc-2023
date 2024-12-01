import re

accepted = []
workflows = {}

def process_workflow(parts, workflow):
    if workflow == "R":
        return
    elif workflow == "A":
        accepted.append(parts)
        return
    workflow = workflows[workflow]
    for instruction in workflow:
        if "condition" in instruction:
            condition = instruction["condition"]
            split = condition[2]
            lower = parts[condition[0]][0]
            upper = parts[condition[0]][1]
            if condition[1] == ">":
                if split <= upper:
                    new_parts = parts.copy()
                    parts[condition[0]] = (lower, split)
                    new_parts[condition[0]] = (split + 1, upper)
                    process_workflow(new_parts, instruction["destination"])
            else:
                if lower <= split:
                    new_parts = parts.copy()
                    parts[condition[0]] = (split, upper)
                    new_parts[condition[0]] = (lower, split - 1)
                    process_workflow(new_parts, instruction["destination"])
        else:
            process_workflow(parts, instruction["destination"])

with open("./19/input.txt", "r", encoding="utf-8") as file:
    while (line := file.readline().rstrip()) != "":
        name, instructions = re.match(r"(\w+){(.+)}", line).groups()
        instructions = instructions.split(",")
        processed = []
        for instruction in instructions:
            instruction = instruction.split(":")
            if len(instruction) == 2:
                category, comparator, value = re.match(r"([xmas])([<>])(\d+)", instruction[0]).groups()
                condition = (category, comparator, int(value))
                instruction = {"condition": condition, "destination": instruction[1]}
            else:
                instruction = {"destination": instruction[0]}
            processed.append(instruction)
        workflows[name] = processed

parts = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
process_workflow(parts, "in")

total = 0
for parts in accepted:
    subtotal = 1
    for lower, upper in parts.values():
        subtotal *= upper - lower + 1
    total += subtotal

print(total)