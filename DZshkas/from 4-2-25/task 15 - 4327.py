from itertools import permutations


def f(x):
    p = 5 <= x <= 40
    q = 41 <= x <= 54
    r = 6 <= x <= 53
    a = a1 <= x <= a2
    return (p or q) and r and not a


ans = []
line = [x / 10 for x in range(40, 550)]

for a1, a2 in permutations(line, 2):
    if all(not f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))