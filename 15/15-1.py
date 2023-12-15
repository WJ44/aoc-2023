sum = 0
with open("./15/input.txt", "r") as file:
    sequence = [line.rstrip() for line in file][0].split(",")
    for step in sequence:
        result = 0
        for c in step:
            result += ord(c)
            result *= 17
            result %= 256
        sum += result

print(sum)