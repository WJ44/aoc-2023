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
    total = 0
    group = groups.pop(0)
    for match in re.finditer(r"(?<=\?|^)([#?]{" + str(group) + r"})(?=\?|$)", spring, overlapped=True):
        new_groups = groups.copy()
        if not "#" in spring[: match.start()]:
            total += find_permutations(spring[match.end() + 1 :], new_groups)
    known[key] = total
    return total


def find_splits(sprs, current_splits, i, j, groups):
    if i >= len(groups) and j >= len(springs):
        return [current_splits]
    if j >= len(sprs):
        return []
    possibilities = []
    current = []
    for l in range(i, len(groups) + 1):
        new_splits = current_splits.copy()
        new_splits.append(current.copy())
        possibilities.extend(find_splits(sprs, new_splits, l, j + 1, groups))
        if l < len(groups) and len(sprs[j]) >= sum(current) + len(current) + groups[i]:
            current.append(groups[l])
        else:
            break
    return possibilities


arrangements = 0
with open("./12/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.rstrip()
        springs, start_groups = line.split()
        start_groups = [int(group) for group in start_groups.split(",")]
        start_groups = start_groups * 5
        springs = ((springs + "?") * 5)[:-1]
        springs = [s for s in springs.split(".") if s]
        subtotal = 0
        splits = find_splits(springs, [], 0, 0, start_groups)
        for split in splits:
            subsubtotal = 1
            for k, s in enumerate(springs):
                subsubtotal *= find_permutations(s, split[k].copy())
            subtotal += subsubtotal
        arrangements += subtotal

print(arrangements)
