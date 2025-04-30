from math import log2

from tqdm import tqdm


def div(x):
    ans = set()
    c = 0
    if int(log2(x)) == log2(x): c += 1
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            d = x // i
            if int(log2(i)) == log2(i):
                c += 1
            else:
                ans.add(i)
            if int(log2(d)) == log2(d):
                c += 1
            else:
                ans.add(d)
    if c >= 20: return sum(ans)
    return False


c = 0

for i in tqdm(range(10 ** 6 + 1, 10 ** 7)):
    d = div(i)
    if d:
        print(i, d)
        c += 1
        if c == 5: break
        # print("*****")
