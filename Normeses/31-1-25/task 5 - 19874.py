def toq(a, q):
    ans = ''
    while a:
        ans += str(a%q)
        a //= q
    return ans[::-1]

ans = []

for n in range(10, 1000000):
    r = toq(n, 3)
    if n%4 == 0: r += r[-3:]
    else: r = '1' + r + "20"
    r = int(r, 3)
    if r > 423:
        ans.append(r)

print(min(ans))