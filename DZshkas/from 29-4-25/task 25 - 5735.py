from math import log2

from tqdm import tqdm


def div(x):
    ans = set()
    c = 0
    flag = True
    if int(log2(x)) == log2(x): c += 1
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            d = x // i
            if int(log2(i)) == log2(i):
                c += 1
            else:
                ans.add(i)
                flag = False
            if int(log2(d)) == log2(d):
                c += 1
            else:
                ans.add(d)
                flag = False
    if c >= 20:
        if flag: return 0
        return sum(ans)
    return -1


c = 0

for i in tqdm(range(10 ** 6 + 1, 10 ** 7)):
    if (d := div(i)) + 1:
        print(i, d)
        c += 1
        if c == 5: break
