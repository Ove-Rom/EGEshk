def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]


n = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005

print(toq(n, 3).count('0'))
