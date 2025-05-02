from itertools import combinations

from tqdm import tqdm


def f(x):
    p = 257 <= x <= 260
    q = 5 <= x <= 100
    r = 99 <= x <= 258
    a = a1 <= x <= a2
    return (a <= r) and ((not (a <= p)) <= q)


line = [i / 5 for i in range(260 * 5)]
ans = []

for a1, a2 in tqdm(combinations(line, 2)):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))
