number = [int(n) for n in input()]

averages_list = [(number[x] + number[x + 1]) / 2 for x in range(len(number) - 1)]

print(averages_list)
