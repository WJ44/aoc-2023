seen = {}
with open("./14/input.txt", "r") as file:
    grid = [[c for c in line.rstrip()] for line in file]
    grid = [list(row) for row in zip(*grid)][::-1]
    k = 0
    while k < 1000000000:
        for _ in range(4):
            for row in grid:
                free = 0
                for i in range(len(row)):
                    if row[i] == ".":
                        pass
                    elif row[i] == "#":
                        free = i + 1
                    elif row[i] == "O":
                        if free == i:
                            free = i + 1
                        else:
                            row[i] = "."
                            row[free] = "O"
                            free = min(free + 1, i)
            grid = [list(row) for row in zip(*grid[::-1])]
        key = tuple([tuple(row) for row in grid])
        if key in seen:
            if "interval" in seen[key]:
                k = k + (1000000000 - (k + 1))//seen[key]["interval"] * seen[key]["interval"]
            else:
                seen[key]["interval"] = k - seen[key]["start"]
        else:
            seen[key] = {"start": k}
        k += 1
    sum = 0
    for row in grid:
        for i in range(len(row)):
            if row[i] == "O":
                sum += len(row) - i
    print(k, sum)