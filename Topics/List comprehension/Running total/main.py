numbers = [int(n) for n in input()]

cumulative_sum = [sum(numbers[:x]) for x in range(1, len(numbers) + 1)]

print(cumulative_sum)
