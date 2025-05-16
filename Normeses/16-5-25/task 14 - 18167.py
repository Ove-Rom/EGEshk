def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

n = 6**900 + 6**10

for x in range(10_000, 0, -1):
    s = toq(n-x, 6)
    if s.count("3") == s.count("5"):
        print(x)
        break