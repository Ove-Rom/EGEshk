def simp(x):
    for i in range(2, round(x ** .5)):
        if x % i == 0:
            return 0
    return 1

for n, i in enumerate(range(194_441, 196_501), start=1):
    if i % 100 == 93 and simp(i):
        print(n, i)