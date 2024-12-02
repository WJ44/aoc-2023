import re

boxes = {}
with open("./15/input.txt", "r", encoding="utf-8") as file:
    sequence = [line.rstrip() for line in file][0].split(",")
    for step in sequence:
        match = re.match(r"([a-z]+)[-=](\d+)?", step)
        label = match.group(1)
        focal_length = match.group(2)
        box = 0
        for c in label:
            box += ord(c)
            box *= 17
            box %= 256
        if box not in boxes:
            boxes[box] = {"labels": [], "focal_lengths": []}
        if label in boxes[box]["labels"]:
            i = boxes[box]["labels"].index(label)
            if not focal_length:
                boxes[box]["labels"].pop(i)
                boxes[box]["focal_lengths"].pop(i)
            else:
                boxes[box]["focal_lengths"][i] = int(focal_length)
        elif focal_length:
            boxes[box]["labels"].append(label)
            boxes[box]["focal_lengths"].append(int(focal_length))

focusing_power = 0
for number, box in boxes.items():
    for slot, focal_length in enumerate(box["focal_lengths"]):
        focusing_power += (number + 1) * (slot + 1) * focal_length

print(focusing_power)
