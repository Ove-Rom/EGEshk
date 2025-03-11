def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]


for x in range(10**10):
    n = 7**666 + 7**333 + 49**x - 343
    n7 = toq(n, 7)
    if n7.count('6') == 49:
        print(x)
        break