import re

workflows = {}
accepted = []
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
    while line := file.readline().rstrip():
        x, m, a, s = re.match(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", line).groups()
        part = {"x": int(x), "m": int(m), "a": int(a), "s": int(s)}
        workflow = workflows["in"]
        while True:
            for instruction in workflow:
                if "condition" in instruction:
                    condition = instruction["condition"]
                    if condition[1] == ">":
                        if part[condition[0]] > condition[2]:
                            destination = instruction["destination"]
                            break
                    else:
                        if part[condition[0]] < condition[2]:
                            destination = instruction["destination"]
                            break
                else:
                    destination = instruction["destination"]
            if destination == "R":
                break
            elif destination == "A":
                accepted.append(part)
                break
            workflow = workflows[destination]

total = 0
for part in accepted:
    total += sum(part.values())
    
print(total)