from collections import Counter

symbols = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
types = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]
hands = []

with open("./7/input.txt", "r") as file:
    for line in file:
        hand, bet = line.split()
        hand = [symbols.index(symbol) for symbol in hand]
        type = types.index(sorted(Counter(hand).values()))
        hands.append(((type, hand), int(bet)))

sum = 0
for i, hand in enumerate(sorted(hands)):
    sum += hand[1] * (i + 1)

print(sum)