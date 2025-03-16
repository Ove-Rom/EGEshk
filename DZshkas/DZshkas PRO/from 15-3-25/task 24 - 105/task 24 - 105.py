from itertools import groupby

data = open("24_105.txt").read()

print(max(len(list(group)) for letter, group in groupby(data)))