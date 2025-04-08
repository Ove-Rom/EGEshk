from string import ascii_uppercase

data = open("24.txt").read()

for i in ascii_uppercase[2:]:
    data = data.replace(i, ' ')

data = data.split()

for i in range(len(data)):
    data[i] = data[i].lstrip('0')
    if not data[i]: data[i] = '0'
    while data[i][-1] in "13579A":
        if len(data[i]) == 1: break
        data[i] = data[i][:-1]

print(len(max(data, key=len)))