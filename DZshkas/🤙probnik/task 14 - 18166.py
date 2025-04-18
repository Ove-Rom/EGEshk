def toq(a, q):
    ans = ""
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

n = 5**2025 + 5**200

ans = []

for x in range(2, 2026):
    s = toq(n - x, 5)
    ans.append([s.count("4"), x])

print(max(ans)[1])
