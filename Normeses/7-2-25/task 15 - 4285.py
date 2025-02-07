from itertools import combinations


def f(x):
    p = 25 <= x <= 240
    q = 170 <= x <= 300
    r = 270 <= x <= 340
    a = a1 <= x <= a2
    return not q or p or a or r

ans = []
line = [x / 5 for x in range(20*5, 345*5)]

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))