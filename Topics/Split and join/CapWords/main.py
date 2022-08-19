text = input().split("_")

corrected = [word.capitalize() for word in text]
print("".join(corrected))
