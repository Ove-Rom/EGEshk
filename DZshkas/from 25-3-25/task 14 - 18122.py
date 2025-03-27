def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]


for x in range(5555, 0, -1):
    n = 5 ** 150 + 5 ** 135 - x
    s = toq(n, 5)
    if s.count('4') == 134:
        print(x)
        break
