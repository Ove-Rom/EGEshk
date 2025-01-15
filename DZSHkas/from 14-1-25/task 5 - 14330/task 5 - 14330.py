from functools import reduce
from operator import mul


for n in range(22229, 100000):
    n = str(n)
    maxx = max(int(i) for i in n)
    minn = min(int(i) for i in n)
    num1 = (minn + maxx)**2
    num2 = reduce(mul, (int(i) if int(i) % 2 == 0 else 1 for i in n))
    if num1 > num2:
        r = str(num1) + str(num2)
    else:
        r = str(num2) + str(num1)
    if r == "12116":
        print(n)
        break