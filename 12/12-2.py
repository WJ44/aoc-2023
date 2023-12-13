import regex as re
from itertools import combinations_with_replacement, permutations
import time

start = time.time()

known = {}

def explore(spring, groups):
    key = (spring, tuple(groups))
    if key in known:
        return known[key]
    if not spring:
        if not groups:
            return 1
        else:
            return 0
    if not groups:
        if not "#" in spring:
            return 1
        else:
            return 0
    sum = 0
    group = groups.pop(0)
    # print(spring, group)
    for match in re.finditer("(?<=\?|^)([#?]{" + str(group) + "})(?=\?|$)", spring, overlapped=True):
        # print(match, match.groups())
        new_groups = groups.copy()
        if not "#" in spring[:match.start()]:
            sum += explore(spring[match.end()+1:], new_groups)
    known[key] = sum
    return sum

def explore2(springs, splits, i, j, groups):
    print(splits)
    if j >= len(springs):
        return []
    possibilities = []
    current = []
    for i in range(i, len(groups)):
        new_splits = splits.copy()
        new_splits.append(current)
        possibilities.extend(explore2(springs, new_splits, i, j+1, groups))
        if len(springs[j]) >= sum(current) + len(current) + groups[i]:
            current.append(groups[i])
        else:
            break
    print(possibilities)
    return possibilities


arrangements = 0
with open("./12/test2.txt", "r") as file:
    for line in file:
        line = line.rstrip()
        print(line)
        springs, groups = line.split()
        groups = [int(group) for group in groups.split(",")]
        # groups = groups*3
        # springs = ((springs + "?")*3)[:-1]
        springs = [s for s in springs.split(".") if s]
        subtotal = 0
        explore2(springs, [], 0, 0, groups)
        # tests = []
        # test = []
        # for i in range(len(groups)):
        #     tests.append((test.copy(), i))
        #     #hoeft niet per se toegevoegd aan lijst, kan gewoon vanaf hier verder, voor volgend spring deel is allen i nodig, dus resultaat kan (aantal mogelijkheden, i) zijn
        #     #alhoewel misschirn eerst checken of combinaties uberhaupt mogelijk zijn, dan kan het ook gewoon  naar alogritme hieronder (behalve eerste gedeelte dan)
        #     if len(springs[0]) >= sum(test) + len(test) + groups[i]:
        #         test.append(groups[i])
        #     else:
        #         break

        print(tests)
        #Now first calculate the way all of these groupings can fit into the first spring bit, then expand the possibilities to the next spring and so on

        # for s in splits:
        #     groups_per_split = []
        #     i = 0
        #     for split in s:
        #         groups_per_split.append(groups[i:i+split])
        #         i += split
        #     # print(groups_per_split)
        #     if any([sum(groups_per_split[j])+len(groups_per_split[j])-1 > len(springs[j]) for j in range(len(springs))]):
        #         continue
        #     ways = []
        #     for i in range(len(springs)):
        #         ways.append(explore(springs[i], groups_per_split[i]))
        #     # print(ways)
        #     subsubtotal = 1
        #     for way in ways:
        #         subsubtotal *= way
        #     subtotal += subsubtotal
        # # print(subtotal)
        # arrangements += subtotal

        
print(arrangements, time.time() - start)