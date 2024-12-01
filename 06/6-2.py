total = 0

with open("./06/input.txt", "r", encoding="utf-8") as file:
    time = int(file.readline().split(":")[1].replace(" ", ""))
    distance = int(file.readline().split(":")[1].replace(" ", ""))
    for i in range(time + 1):
        if i * (time - i) > distance:
            total += 1

print(total)
