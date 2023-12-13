sum = 0
with open("./13/input.txt", "r") as file:
    patterns = [pattern.split("\n") for pattern in file.read().split("\n\n")]
    for pattern in patterns:
        for i in range(1, len(pattern)):
            symmetry = True
            for j in range(i):
                if i+j < len(pattern) and i-j > 0:
                    if not pattern[i-1-j] == pattern[i+j]:
                        symmetry = False
                        break
                else:
                    break
            if symmetry:
                sum += 100 * i
                break
        for i in range(1, len(pattern[0])):
            symmetry = True
            for j in range(i):
                if i+j < len(pattern[0]) and i-j > 0:
                    column1 = [row[i-1-j] for row in pattern]
                    column2 = [row[i+j] for row in pattern]
                    if not column1 == column2:
                        symmetry = False
                        break
                else:
                    break
            if symmetry:
                sum += i
                break

print(sum)