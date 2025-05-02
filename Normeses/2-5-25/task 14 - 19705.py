def toq(a, q):
    ans = ""
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

n = 43**56 + 113**841

for x in range(2005, 0, -1):
    s = toq(n - x, 4)
    c1 = sum(s.count(i) for i in "02") % 2 == 0
    c2 = sum(s.count(i) for i in "13") % 2 == 0
    c3 = s.count("2") <= 712
    if c1 and c2 and c3:
        print(x)
        break