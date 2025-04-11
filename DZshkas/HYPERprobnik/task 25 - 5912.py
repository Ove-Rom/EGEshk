from fnmatch import fnmatch
import tqdm

def div(x):
    ans = set()
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            ans |= {i, x // i}
    if len(ans) == 18:
        return max(ans)
    return 0


for i in tqdm.tqdm(range(120445, 10 ** 7)):
    if fnmatch(str(i), "12?*45"):
        d = div(i)
        if d:
            print(i, d)
