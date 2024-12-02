from collections import Counter

symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
kinds = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]
hands = []

with open("./07/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        hand, bet = line.split()
        hand = [symbols.index(symbol) for symbol in hand]
        kind = kinds.index(sorted(Counter(hand).values()))
        hands.append(((kind, hand), int(bet)))

total = 0
for i, hand in enumerate(sorted(hands)):
    total += hand[1] * (i + 1)

print(total)
