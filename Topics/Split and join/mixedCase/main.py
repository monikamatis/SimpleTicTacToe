text = input().split()

corrected = [text[0].lower()] + [text[x].capitalize() for x in range(1, len(text))]

print("".join(corrected))
