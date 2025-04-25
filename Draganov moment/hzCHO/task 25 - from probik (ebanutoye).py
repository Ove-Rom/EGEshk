def isp(x):
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            return False
    return True

def div(x):
    ans = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            if isp(i): ans.add(i)
            if isp(x // i): ans.add(x // i)
    if ans: return sum(ans) // len(ans)
    return 0

ans = []
c = 0

for i in range(9_500_001, 10**10):
    f = div(i)
    if f and f % 813 == 0:
        ans.append([f, i])
        c += 1
        if c == 5: break

for i in sorted(ans):
    print(*reversed(i))
