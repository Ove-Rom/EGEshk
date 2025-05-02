def d(a, b):
    return a % b == 0

c = 0


for a in range(1, 1_001):
    if all(d(a, 12) and (d(530, x) <= ((not d(a, x)) <= (not d(170, x)))) for x in range(1, 1_000)):
        c += 1

print(c)