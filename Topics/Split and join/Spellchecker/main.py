dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

text = input().split()
i = 0
for word in text:
    if word in dictionary:
        i += 1
        continue
    else:
        print(word)

if i == len(text):
    print("OK")
