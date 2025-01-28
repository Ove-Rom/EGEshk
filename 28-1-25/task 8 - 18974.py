from string import digits, ascii_lowercase

alph = digits + ascii_lowercase


def toq(a, q):
    ans = ''
    while a:
        ans += alph[a % q]
        a //= q
    return ans[::-1]


count = 0

for i in range(int("1000", 25), int("10000", 25)):
    n = toq(i, 25)
    c1 = sum(int(j, 25) % 2 for j in n) == 1
    c2 = sum(int(j, 25) <= 5 for j in n) <= 2
    if c1 & c2: count += 1

print(count)
