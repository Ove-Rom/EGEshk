v = set()
c = 0


def f(a):
    global c, v
    if not (-50 <= a <= 50): return
    if a in v: return
    if a == 30:
        c += 1
        return
    v.add(a)
    f(a + 2)
    f(a - 3)
    v.discard(a)


f(1)
print(c)
