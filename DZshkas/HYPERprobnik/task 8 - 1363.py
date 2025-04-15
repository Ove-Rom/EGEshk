def toq(a, q):
    ans = ""
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

c = 0

for i in range(int("300001", 5), int("400000", 5), 2):
    n = toq(i, 5)
    if n[0] == "3": c += 1

print(c)