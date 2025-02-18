from fnmatch import fnmatch
from functools import reduce
from operator import mul

def div(x):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1

for i in range(315670, 10**7):
    if div(i) and fnmatch(str(i), "31*567?"):
        print(i, reduce(mul, [int(j) for j in str(i)]))
