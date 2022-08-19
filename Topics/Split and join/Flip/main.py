sequence = input().split()

corrected = [sequence[-x] for x in range(1, len(sequence) + 1)]

print(" ".join(corrected))
