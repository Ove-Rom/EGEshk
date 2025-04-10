from itertools import combinations


def f(x):
    p = 5 <= x <= 30
    q = 14 <= x <= 23
    a = a1 <= x <= a2
    return (p == q) <= (not a)

line = [i / 5 for i in range(35*5)]
ans = []

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(max(ans))