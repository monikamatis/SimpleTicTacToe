text = input().split()
printout = [word for word in text if word.endswith("s")]

print("_".join(printout))
