from itertools import groupby

data = open("24_4682.txt").read()

for i in "AE":
    data = data.replace(i, 'g')

for i in "BCD":
    data = data.replace(i, 's')

data = data.replace("gs", '*')

print(max(len(list(group)) for letter, group in groupby(data) if letter == '*'))