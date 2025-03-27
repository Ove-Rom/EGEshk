from string import ascii_uppercase

data = open("24_10724.txt").read()

for i in ascii_uppercase[6:]:
    data = data.replace(i, ' ')

data = data.split()

for i in range(len(data)):
    data[i] = data[i].lstrip('0')

print(len(max(data, key=len)))