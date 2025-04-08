with open("26.txt") as f:
    n = f.readline()
    data = [int(i) for i in f]

data = sorted(data, reverse=True)

c = 1
curl = data[0]

for i in data[1:]:
    if curl - i >= 9:
        c += 1
        curl = i

print(c, curl)