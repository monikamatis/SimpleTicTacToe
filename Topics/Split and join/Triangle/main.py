number = int(input())

char = ["#" * ((x * 2) - 1) for x in range(1, number + 1)]
triangle = [char[x].center(len(char[-1])) for x in range(number)]
print("\n", "\n".join(triangle))
