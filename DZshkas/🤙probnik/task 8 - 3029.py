from itertools import product, repeat

from tqdm import tqdm


def toq(a, q):
    ans = ""
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

trip = [i * 3 for i in "012345678"]

c = 0

for i in tqdm(range(int("1000000", 9), int("10000000", 9))):
    n = toq(i, 9)
    c1 = n[-1] not in "347"
    c2 = not any(j in n for j in trip)
    if c1 and c2:
        c += 1
print(c)

c = 0

for i in tqdm(product("012345678", repeat=7)):
    i = "".join(i).lstrip("0")
    if len(i) != 7: continue
    c1 = i[-1] not in "347"
    c2 = not any(j in i for j in trip)
    if c1 and c2:
        c += 1

print(c)
