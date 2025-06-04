def d(z, v): return z % v == 0

for a in range(1, 10_000):
    if all(d(x, 2) <= (not d(x, 3)) or (x + a >= 80) for x in range(1, 1_000)):
        print(a)
        break