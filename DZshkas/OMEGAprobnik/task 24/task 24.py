with open("24_8510.txt") as f:
    data = f.read()

data = data.replace('N', '*')
data = data.replace('P', '*')
data = data.replace('O', '*')

data = data.split('*')

maxLen = 0

for i in range(len(data)-2):
    maxLen = max(len(data[i]) + len(data[i+1]) + len(data[i+2]), maxLen)

print(maxLen)