from string import digits, ascii_lowercase

alph = digits + ascii_lowercase


def toq(a, q):
    ans = ''
    while a:
        ans += alph[a % q]
        a //= q
    return ans[::-1]


pattern = ''.join([str(i % 2 == 0) for i in range(8)])
count = 0

for i in range(int("1000000", 12), int("10000000", 12)):
    n = toq(i, 12)
    c1 = n.count('b') == 2
    c2 = ''.join(str(int(i, 12) % 2 == 0) for i in n) in pattern
    if c1 & c2: count += 1

print(count)
