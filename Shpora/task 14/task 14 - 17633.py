def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

n = 6**260 + 6**160 + 6**60

for x in range(2031):
    if toq(n-x, 6).count("0") == 202:
        print(x)
        break