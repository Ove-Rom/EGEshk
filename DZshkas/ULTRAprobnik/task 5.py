def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]


ans = []

for n in range(100_000):
    r = toq(n, 4)
    if len(r) % 2 == 0: r = r[:len(r) // 2] + '0' + r[len(r) // 2:]
    if int(r) <= 180: ans.append(n)

print(max(ans))
