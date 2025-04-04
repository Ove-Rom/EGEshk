def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

for x in range(1000):
    n = 7**666 + 7**333 + 49**x - 343
    s = toq(n, 7)
    if s.count('6') == 49:
        print(x)
        break