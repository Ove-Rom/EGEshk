def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

for x in range(1, 2005)[::-1]:
    n = toq(43**56 + 113**841 - x, 4)
    c1 = sum(int(i) % 2 == 0 for i in n) % 2 == 0
    c2 = sum(int(i) % 2 != 0 for i in n) % 2 != 0
    c3 = sum(int(i) == 2 for i in n) <= 712
    if c1 and c2 and c3:
        print(x)
        break