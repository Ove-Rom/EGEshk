def f(a1, a2):
    P = [p for p in range(15, 41)]
    Q = [q for q in range(21, 64)]
    for x in range(1000):
        f1 = (x in P) <= (((x in Q) and not (a1 <= x <= a2)) <= (not x in P))
        if not f1:
            return 0
    else: return 1

ans = []
for start in range(100):
    for stop in range(100):
        if f(start, stop):
            ans.append(stop - start)

print(min(ans))