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
            sequences[i].append(sequences[i][len(sequences[i]) - 1] + sequences[i + 1][len(sequences[i + 1]) - 1])
        total += sequences[0][len(sequences[0]) - 1]

print(total)
