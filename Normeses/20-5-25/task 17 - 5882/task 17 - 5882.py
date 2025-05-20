with open("17_5882.txt") as f:
    data = [int(i) for i in f]

mins = 0

for n1, n2 in zip(data, data[1:]):
    if (str(n1)[-1] == "3") ^ (str(n2)[-1] == "3"):
        mins = min(n1, n2, mins)

minN = sum(int(i)**2 for i in str(abs(mins)))


c = []

for i in data:
    c1 = "3" in str(i)
    c2 = i >= minN
    if c1 and c2:
        c.append(i)

print(len(c), min(c))
