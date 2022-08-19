lines = int(input())
results = [input() for n in range(lines)]
wins = [name.split() for name in results if name.endswith("win")]
print([wins[n][0] for n in range(len(wins))])
print(len(wins))
