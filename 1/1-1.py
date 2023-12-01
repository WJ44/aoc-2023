calibration_sum = 0

with open("./1/input.txt", "r") as file:
    for line in file:
        first = ""
        last = ""
        for c in line:
            if c.isdigit():
                if not first:
                    first = c
                last = c
        calibration = int(first + last)
        calibration_sum += calibration

print(calibration_sum)