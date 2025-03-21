def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

for n in range(10**5):
    r = toq(n, 3)
    if sum(int(i) for i in r) % 3 == 0:
        r += '0'
        r = '12' + r[2:]
    else:
        r += '2'
        r = '10' + r[2:]
    r = int(r, 3)
    if r > 105:
        print(n); break