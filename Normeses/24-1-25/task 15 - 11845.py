def f(a):
    for x in range(1, 1000):
        f1 = ((a % x == 0) <= ((x == a) or (x == 1)))
        if not f1: return 0
    else: return 1

count = 0

for a in range(1, 11_111):
    if f(a):
        count += 1
print(count)