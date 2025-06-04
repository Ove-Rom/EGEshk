def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

n = 4**210 + 4**110
ans = []

for x in range(1, 3_001):
    s = toq(n-x, 4).count("0")
    ans.append([s, x])

print(sorted(ans, key=lambda x: [-x[0], x[1]]))