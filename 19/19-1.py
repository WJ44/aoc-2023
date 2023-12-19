import re

workflows = {}

with open("./19/test.txt", "r") as file:
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
    print(workflows)
    while line := file.readline().rstrip():
        x, m, a, s = re.match(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", line).groups()
        part = {"x": int(x), "m": int(m), "a": int(a), "s": int(s)}
        workflow = workflows["in"]
        while True:
            for instruction in workflow:
                if "condition" in instruction:
                    if condition[2] == ">":
                        print(part[condition[0]] > condition[2])
                    else:
                        print(part[condition[0]] < condition[2])
                else:
                    print(True)

