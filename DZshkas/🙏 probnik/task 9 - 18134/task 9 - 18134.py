with open("task 9 - 18134.txt") as f:
    data = [list(map(int, i.split())) for i in f]

ans = 0

for i in data:
    pov = {j: 0 for j in set(i)}
    for j in i:
        pov[j] += 1
    c1 = list(pov.values()).count(2) == 2
    c2 = list(pov.values()).count(1) == 2
    maxN = 0
    mul = 1
    for n, c in pov.items():
        if c != 1:
            maxN = max(maxN, n)
        else:
            mul *= n
    c3 = maxN ** 2 > mul
    if c1 and c2 and c3:
        ans += 1

print(ans)
