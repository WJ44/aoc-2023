calibration_sum = 0

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("./1/input.txt", "r") as file:
    for line in file:
        for digit, text in enumerate(digits, 1):
            line = line.replace(text, text + str(digit) + text)
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