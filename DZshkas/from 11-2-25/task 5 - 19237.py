def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

ans = []

for n in range(1, 10000):
    r = toq(n, 3)
    if n % 3 == 0: r += r[-2:]
    else: r += toq(sum(int(i) for i in r), 3)
    r = int(r, 3)
    if r % 2 == 0 and r > 220:
        ans.append(r)

print(min(ans))