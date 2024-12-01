import re

total = 0

with open("./04/input.txt", "r", encoding="utf-8") as file:
    copies = {}
    for line in file:
        m = re.match(r"Card[\s]+(\d+):([\s\d+]+)\s\|([\s\d+]+)", line)
        card = int(m.group(1))
        if card not in copies:
            copies[card] = 0
        copies[card] += 1
        wins = 0
        winning = [int(i) for i in m.group(2).split()]
        own = [int(i) for i in m.group(3).split()]
        result = 0
        for number in own:
            if number in winning:
                wins += 1
        for i in range(wins):
            copy = card + 1 + i
            if copy not in copies:
                copies[copy] = 0
            copies[copy] += copies[card]
        total += copies[card]

print(total)
