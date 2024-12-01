total = 0

with open("./09/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        sequences = []
        sequence = [int(n) for n in line.split()]
        sequences.append(sequence)
        while any(i != 0 for i in sequence):
            sequence = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
            sequences.append(sequence)
        for i in range(len(sequences) - 2, -1, -1):
            sequences[i].insert(0, sequences[i][0] - sequences[i + 1][0])
        total += sequences[0][0]

print(total)
