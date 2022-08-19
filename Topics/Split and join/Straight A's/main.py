grades = input().split()

a_grades = [x for x in grades if x == "A"]
print(round(len(a_grades) / len(grades), 2))
