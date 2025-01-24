from zoneinfo import reset_tzpath


def f(a):
    for x in range(1000):
        f1 = (x & a == 0) or not (x & 32 == 0) or not (x & 12 == 0)
        if not f1: return 0
    else: return 1

for a in range(1000, 0, -1):
    if f(a):
        print(a)
        break
