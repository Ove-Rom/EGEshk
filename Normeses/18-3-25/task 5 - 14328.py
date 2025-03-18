from string import digits, ascii_lowercase

alph = digits+ascii_lowercase

def toq(a, q):
    ans = ''
    while a:
        ans += alph[a % q]
        a //= q
    return ans[::-1]

ans = []

for n in range(10**5):
    r = toq(n, 12)
    if n % 3 == 0: r = '1' + r + 'b'
    else: r = '2' + r + '0'
    r = int(r, 12)
    if r < 1996: ans.append(r)

print(max(ans))