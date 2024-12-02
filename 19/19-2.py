import re

accepted = []
workflows = {}


def process_workflow(parts, workflow):
    if workflow == "R":
        return
    if workflow == "A":
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
        name, insts = re.match(r"(\w+){(.+)}", line).groups()
        insts = insts.split(",")
        processed = []
        for inst in insts:
            inst = inst.split(":")
            if len(inst) == 2:
                category, comparator, value = re.match(r"([xmas])([<>])(\d+)", inst[0]).groups()
                cond = (category, comparator, int(value))
                inst = {"condition": cond, "destination": inst[1]}
            else:
                inst = {"destination": inst[0]}
            processed.append(inst)
        workflows[name] = processed

start_parts = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
process_workflow(start_parts, "in")

total = 0
for good_parts in accepted:
    subtotal = 1
    for low, up in good_parts.values():
        subtotal *= up - low + 1
    total += subtotal

print(total)
