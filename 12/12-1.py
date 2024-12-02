import re


def explore(string, unknowns, r, r2):
    if not re.fullmatch(r2, string):
        return 0
    if not unknowns:
        if re.fullmatch(r, string):
            return 1
        return 0
    subtotal = 0
    unknown = unknowns.pop()
    subtotal += explore(string[:unknown] + "." + string[unknown + 1 :], unknowns.copy(), r, r2)
    subtotal += explore(string[:unknown] + "#" + string[unknown + 1 :], unknowns.copy(), r, r2)
    return subtotal


total = 0
with open("./12/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.rstrip()
        springs, groups = line.split()
        groups = [int(group) for group in groups.split(",")]
        regex = r"[.]*"
        for group in groups:
            regex = regex + r"([#]{" + str(group) + r"})[.]+"
        regex = regex[: len(regex) - 1] + r"*"
        regex2 = r"[.?]*"
        for group in groups:
            regex2 = regex2 + r"([#?]{" + str(group) + r"})[.?]+"
        regex2 = regex2[: len(regex2) - 1] + r"*"
        start_unknowns = [i for i, c in enumerate(springs) if c == "?"]
        total += explore(springs, start_unknowns, regex, regex2)

print(total)
