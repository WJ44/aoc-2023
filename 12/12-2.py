import re
from itertools import combinations_with_replacement, permutations

arrangements = 0
with open("./12/test.txt", "r") as file:
    for line in file:
        line = line.rstrip()
        print(line)
        springs, groups = line.split()
        groups = [int(group) for group in groups.split(",")]
        springs = [s for s in springs.split(".") if s]
        #TODO all possible ways to split the groups over de different parts of the springs
        splits = [item for permutation in [set(permutations(combination)) for combination in combinations_with_replacement(range(len(groups)+1), len(springs))if sum(combination) == len(groups)] for item in permutation]
        print(splits)
        subtotal = 0
        for s in splits:
            groups_per_split = []
            i = 0
            for split in s:
                groups_per_split.append(groups[i:i+split])
                i += split
            print(groups_per_split)
            if any([sum(groups_per_split[j])+len(groups_per_split[j])-1 > len(springs[j]) for j in range(len(springs))]):
                continue
            for group in groups_per_split:
                #TODO amount of ways to put the correct division of #s in the corresponding split

            subtotal += 1
        print(subtotal)

        
print(arrangements)