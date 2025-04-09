def toq(a, q):
    ans = ""
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

ans = []

for n in range(1, 10**7):
    r = toq(n, 3)
    if n % 5 == 0:
        r += r[-3:]
    else:
        r += toq((n % 5) * 5 ,3)
    r = int(r, 3)
    if r < 5496: ans.append(n)


print(max(ans))