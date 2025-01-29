def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

ans = []

for n in range(10000):
    r = toq(n, 4)
    if n % 4 == 0:
        r = '2' + r + "03"
    else:
        r += toq((n%4)*5, 4)
    r = int(r, 4)
    if r <= 567:
        ans.append(n)
print(max(ans))