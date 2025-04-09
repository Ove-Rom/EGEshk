def toq(a, q):
    ans = ""
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

c = 0

for i in range(int("300000", 5), int("400000", 5)):
    n = toq(i, 5)
    c1 = sum(int(j) for j in n) % 2 == 0
    c2 = n[0] == "3"
    if c1 and c2: c += 1

print(c)