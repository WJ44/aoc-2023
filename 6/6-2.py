sum = 0

with open("./6/input.txt", "r") as file:
    time = int(file.readline().split(":")[1].replace(" ", ""))
    distance = int(file.readline().split(":")[1].replace(" ", ""))
    for i in range(time + 1):
        if i * (time - i) > distance:
            sum += 1

print(sum)