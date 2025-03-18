from string import digits, ascii_lowercase

alph = digits+ascii_lowercase

def toq(a, q):
    ans = ''
    while a:
        ans += alph[a % q]
        a //= q
    return ans[::-1]

for x in range(2005, 0, -1):
    n = 4 ** 163 * 5 + 12 ** 62 - x
    n = toq(n, 5)
    if n.count('1') < n.count('4'):
        print(x)
        break