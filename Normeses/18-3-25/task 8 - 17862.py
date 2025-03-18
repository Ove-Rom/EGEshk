from string import digits, ascii_lowercase

alph = digits+ascii_lowercase

def toq(a, q):
    ans = ''
    while a:
        ans += alph[a % q]
        a //= q
    return ans[::-1]

c = 0

for i in range(int("10000", 12), int("100000", 12)):
    n = toq(i, 12)
    if n.count('7') == 1:
        if sum(int(s, 12) > 8 for s in n) <= 3:
            c += 1

print(c)