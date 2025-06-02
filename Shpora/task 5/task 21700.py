def toq(a, q):
    ans = ""
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

for n in range(10000, 2, -1):
    r = toq(n, 3)
    if n % 3 == 0:
        r += r[-1] * 2
    else:
        r += toq(n % 3 * 3, 3)
    r = int(r, 3)
    if r <= 150:
        print(n)
        break