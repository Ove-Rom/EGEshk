def tr(n, m, k):
    if max(n, m, k) > sum([n, m, k]) - max(n, m, k):
        return 1
    else: return 0

for a in range(1000)[::-1]:
    if all(tr(a, 7, x) <= ((max(x + 5, 14) <= 27) == (not tr(36, 21, x))) for x in range(1000)):
        print(a)
        break
