import re

solution = 0

with open("./04/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        m = re.match(r"Card[\s]+\d+:([\s\d+]+)\s\|([\s\d+]+)", line)
        winning = [int(i) for i in m.group(1).split()]
        own = [int(i) for i in m.group(2).split()]
        result = 0
        for number in own:
            if number in winning:
                if not result:
                    result = 1
                else:
                    result *= 2
        solution += result

print(solution)
