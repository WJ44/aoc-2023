calibration_sum = 0

with open("./01/input.txt", "r", encoding="utf-8") as file:
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
