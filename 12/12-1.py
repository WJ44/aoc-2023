import re
import time

start = time.time()

def explore(string, unknowns, regex, regex2):
    if not re.fullmatch(regex2, string):
        return 0
    if not unknowns:
        if re.fullmatch(regex, string):
            return 1
        else:
            return 0
    sum = 0
    unknown = unknowns.pop()
    sum += explore(string[:unknown] + "." + string[unknown+1:], unknowns.copy(), regex, regex2)
    sum += explore(string[:unknown] + "#" + string[unknown+1:], unknowns.copy(), regex, regex2)
    return sum

sum = 0
with open("./12/input.txt", "r") as file:
    for line in file:
        line = line.rstrip()
        springs, groups = line.split()
        groups = [int(group) for group in groups.split(",")]
        regex = "[.]*"
        for group in groups:
            regex = regex + "([#]{" + str(group) + "})[.]+"
        regex = regex[:len(regex) - 1] + "*"
        regex2 = "[.?]*"
        for group in groups:
            regex2 = regex2 + "([#?]{" + str(group) + "})[.?]+"
        regex2 = regex2[:len(regex2) - 1] + "*"
        unknowns = [i for i, c in enumerate(springs) if c == "?"]
        sum += explore(springs, unknowns, regex, regex2)

print(sum, time.time() - start)