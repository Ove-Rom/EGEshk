def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]


for x in range(1, 2031)[::-1]:
    n = 3 ** 100 - x
    s = toq(n, 3)
    if s.count('0') == 1:
        print(x)
        break
