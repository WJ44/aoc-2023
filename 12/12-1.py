with open("./12/test.txt", "r") as file:
    for line in file:
        springs, groups = line.split()
        groups = [int(group) for group in groups.split(",")]
        splits = [split for split in springs.split(".") if split]
        remaining = len(groups) - len(splits)
        test = []
        for i in range(remaining + 1):
            test.append([i])
        print(test)
        new_test = []
        for t in test:
            for i in range(remaining + 1 - sum(t)):
                new_t = t.copy()
                new_t.append(i)
                new_test.append(new_t)
        print(new_test)