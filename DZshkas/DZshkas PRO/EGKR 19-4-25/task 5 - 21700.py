def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

ans = []

for n in range(3, 10**3):
    r = toq(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += toq((n % 3) * 3, 3)
    r = int(r, 3)
    if r <= 150:
        ans.append(n)

print(max(ans))