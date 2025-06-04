def d(z, v): return z % v == 0

for a in range(1_000, 0, -1):
    if all(d(x, a) or ((60 <= x <= 80) <= (not d(x, 22))) for x in range(1, 1_000)):
        print(a)
        break