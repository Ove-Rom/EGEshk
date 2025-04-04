d = [list(map(int, i.split())) for i in open("9_4614.txt")]

c = 0

for i in d:
    c1 = max(i) < sum(i) - max(i)
    c2 = len(i) == len(set(i)) + 1
    if c1 and c2: c += 1

print(c)