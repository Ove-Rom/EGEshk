from itertools import product

for num, i in enumerate(product(sorted("привычка"), repeat=5)):
    if num % 5 == 0:
        continue
    c1 = len(set(i)) == 5
    c2 = all(j in "првчк" for j in i)
    if c1 & c2:
        print(num - num // 5)
        break
