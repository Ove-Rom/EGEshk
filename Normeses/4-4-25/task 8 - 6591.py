def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]


c = 0

for i in range(int("10000", 7), int("100000", 7)):
    s = toq(i, 7)
    c1 = s.count('6') == 1
    s1 = sum(int(j) for j in s if j in "13579")
    s2 = sum(int(j) for j in s if j in "2468")
    c2 = s2 < s1
    if c1 and c2:
        c += 1
print(c)