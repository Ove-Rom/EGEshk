def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

n = 7**170 + 7**100
ans = []

for x in range(2030, 0, -1):
    ans.append([toq(n-x, 7).count("0"), x])

print(max(ans)[1])