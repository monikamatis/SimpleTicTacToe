numbers = str(input())
numbers_list = numbers.split()

x = input()

indexes = [str(index) for index in range(len(numbers_list)) if numbers_list[index] == x]
if indexes:
    print(" ".join(indexes))
else:
    print("not found")
