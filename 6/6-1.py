product = 1

with open("./6/input.txt", "r") as file:
    times = [int(time) for time in file.readline().split(":")[1].split()]
    distances = [int(distance) for distance in file.readline().split(":")[1].split()]
    for time, distance in zip(times, distances):
        sum = 0
        for i in range(time + 1):
            if i * (time - i) > distance:
                sum += 1
        product *= sum

print(product)