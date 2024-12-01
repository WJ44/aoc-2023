from collections import Counter

symbols = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
kinds = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]
hands = []

with open("./07/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        hand, bet = line.split()
        counts = Counter(hand)
        if counts.most_common(1)[0][1] != 5:
            Js = counts['J']
            del counts['J']
            for i in range(Js):
                counts[counts.most_common(1)[0][0]] += 1
        hand = [symbols.index(symbol) for symbol in hand]
        kind = kinds.index(sorted(counts.values()))
        hands.append(((kind, hand), int(bet)))

total = 0
for i, hand in enumerate(sorted(hands)):
    total += hand[1] * (i + 1)

print(total)
