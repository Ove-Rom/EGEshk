from itertools import groupby

data = open("24_4643.txt").readline()

data = data.replace('2', '1').replace('B', 'A')
data = data.replace('1', '+').replace('A', '-')
data = data.replace("++-", '*')

print(max(len(list(group)) for letter, group in groupby(data) if letter == '*'))
