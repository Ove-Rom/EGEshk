from string import digits, ascii_lowercase

alph = digits + ascii_lowercase
c = 0


def toq(a, q):
    ans = ''
    while a:
        ans += alph[a % q]
        a //= q
    return ans


for n in range(int("10000", 16), int("100000", 16)):
    r = '0' + toq(n, 16) + '0'
    c1 = r.count('6') == 2
    c2 = all((r[i - 1] != '6' and r[i + 1] != '6') for i in range(1, len(r) - 1) if int(r[i], 16) % 2 == 0)
    if c1 & c2:
        c += 1

print(c)
