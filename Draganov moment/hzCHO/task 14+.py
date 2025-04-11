def toq(a, q):
    ans = ""
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

num = 4**163 * 5 + 12**62
for x in range(2005, 0, -1):
    n = num - x
    n = toq(n, 5)
    if n.count("1") < n.count("4"):
        print(x)
        break
