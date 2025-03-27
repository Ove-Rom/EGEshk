from itertools import combinations


def f(x):
    p = 1 <= x <= 98
    q = 25 <= x <= 42
    a = a1 <= x <= a2
    return not q or (p or not q or a)


ans = []
line = [i / 5 for i in range(0, 100 * 5)]

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))
