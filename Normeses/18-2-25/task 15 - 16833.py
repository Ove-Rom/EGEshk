from itertools import combinations


def f(x):
    p = 25 <= x <= 73
    q = 75 <= x <= 118
    a = a1 <= x <= a2
    return not a or q or p

line = [i / 5 for i in range(20*5, 125*5)]
ans = []

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(max(ans))