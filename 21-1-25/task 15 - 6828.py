def f(a1, a2):
    P = [p for p in range(257, 257)]
    Q = [q for q in range(5, 601)]
    R = [r for r in range(59, 229)]
    for x in range(1000):
        f1 = ((x in R) <= (a1 <= x <= a2)) or (((x % 3 == 0) <= (x in P)) <= ((x in Q) <= (a1 <= x <= a2)))
        if not f1: return 0
    else: return 1

ans = []

for a1 in range(1000):
    for a2 in range(1000):
        if f(a1, a2):
            ans.append(a2 - a1)

print(min(ans))