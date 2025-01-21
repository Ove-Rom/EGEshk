def f(a):
    ans = []
    for x in range(1, 1000):
            for y in range(1, 1000):
                f1 = (x + y <= 22) or (y <= x - 6) or (y >= a)
                ans.append(f1)
    return all(ans)

for a in range(1000, 0, -1):
    if f(a):
        print(a)
        break