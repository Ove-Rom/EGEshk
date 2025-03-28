def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

ans = []

for n in range(100000):
    r = toq(n, 3)
    match sum(int(i) for i in r) % 2:
        case 0: r = '1' + r + '2'
        case 1: r = '2' + r + '0'
    r = int(r, 3)
    if r > 100: ans.append(r)

print(min(ans))