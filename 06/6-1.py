total = 1

with open("./06/input.txt", "r", encoding="utf-8") as file:
    times = [int(time) for time in file.readline().split(":")[1].split()]
    distances = [int(distance) for distance in file.readline().split(":")[1].split()]
    for time, distance in zip(times, distances):
        subtotal = 0
        for i in range(time + 1):
            if i * (time - i) > distance:
                subtotal += 1
        total *= subtotal

print(total)
