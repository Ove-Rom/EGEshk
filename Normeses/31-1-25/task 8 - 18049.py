def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]


count = 0

for i in range(int("1000000", 9), int("10000000", 9)):
    j = str(i)
    c1 = j[0] not in "246"
    c2 = j[-3:] != j[0] * 3
    if c1 & c2: count += 1

print(count)
