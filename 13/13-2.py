sum = 0
with open("./13/input.txt", "r", encoding="utf-8") as file:
    patterns = [pattern.split("\n") for pattern in file.read().split("\n\n")]
    for pattern in patterns:
        for i in range(1, len(pattern)):
            difference = 0
            for j in range(i):
                if i+j < len(pattern) and i-j > 0:
                    for p1, p2 in zip(pattern[i-1-j], pattern[i+j]):
                        if p1 != p2:
                            difference += 1
                            if difference > 1:
                                break
                else:
                    break
            if difference == 1:
                sum += 100 * i
                break
        for i in range(1, len(pattern[0])):
            difference = 0
            for j in range(i):
                if i+j < len(pattern[0]) and i-j > 0:
                    column1 = [row[i-1-j] for row in pattern]
                    column2 = [row[i+j] for row in pattern]
                    for p1, p2 in zip(column1, column2):
                        if p1 != p2:
                            difference += 1
                            if difference > 1:
                                break
                else:
                    break
            if difference == 1:
                sum += i
                break

print(sum)