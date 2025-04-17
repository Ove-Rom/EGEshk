with open("task 9 - 6262.txt") as f:
    data = [list(map(int, i.split())) for i in f]

c = 0

for i in data:
    c1 = len(set(i)) != len(i)
    c2 = sum(j % 2 for j in i) == 3
    if c1 ^ c2: c += 1

print(c)