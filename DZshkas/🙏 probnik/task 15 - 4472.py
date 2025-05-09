from itertools import combinations

from tqdm import tqdm


def f(x):
    p = 254 <= x <= 800
    q = 410 <= x <= 823
    a = a1 <= x <= a2
    return (p and not a) <= q

line = [i/5 for i in range(250*5, 825*5)]
ans = []

for a1, a2 in tqdm(combinations(line, 2)):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))