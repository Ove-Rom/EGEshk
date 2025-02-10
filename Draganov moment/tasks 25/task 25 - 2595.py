from functools import reduce
from operator import mul

def div(x):
    ans = set()
    for i in range(2, round(x ** 0.5) + 1):
        if x%i == 0:
            ans.add(i)
            ans.add(x//i)
    return sorted(ans)

count = 0

for i in range(400_000_000, 10**10):
    divs = div(i)
    if len(divs) >= 5:
        m = reduce(mul, divs[:5])
        if str(m)[-2:] == "17" and m <= i:
            count+= 1
            print(m, divs[4])
            if count == 5: break