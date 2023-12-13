import regex as re

known = {}
def find_permutations(spring, groups):
    if not spring:
        return 1 if not groups else 0
    if not groups:
        return 1 if not "#" in spring else 0
    key = (spring, tuple(groups))
    if key in known:
        return known[key]
    sum = 0
    group = groups.pop(0)
    for match in re.finditer("(?<=\?|^)([#?]{" + str(group) + "})(?=\?|$)", spring, overlapped=True):
        new_groups = groups.copy()
        if not "#" in spring[:match.start()]:
            sum += find_permutations(spring[match.end()+1:], new_groups)
    known[key] = sum
    return sum

def find_splits(springs, splits, i, j, groups):
    if i >= len(groups) and j >= len(springs):
        return [splits]
    if j >= len(springs):
        return []
    possibilities = []
    current = []
    for i in range(i, len(groups)+1):
        new_splits = splits.copy()
        new_splits.append(current.copy())
        possibilities.extend(find_splits(springs, new_splits, i, j+1, groups))
        if i < len(groups) and len(springs[j]) >= sum(current) + len(current) + groups[i]:
            current.append(groups[i])
        else:
            break
    return possibilities

arrangements = 0
with open("./12/input.txt", "r") as file:
    for line in file:
        line = line.rstrip()
        springs, groups = line.split()
        groups = [int(group) for group in groups.split(",")]
        groups = groups*5
        springs = ((springs + "?")*5)[:-1]
        springs = [s for s in springs.split(".") if s]
        subtotal = 0
        splits = find_splits(springs, [], 0, 0, groups)
        for split in splits:
            subsubtotal = 1
            for i in range(len(springs)):
                subsubtotal *= find_permutations(springs[i], split[i].copy())
            subtotal += subsubtotal
        arrangements += subtotal
        
print(arrangements)