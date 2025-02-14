from string import digits, ascii_lowercase

alph = digits + ascii_lowercase
def toq(a, q):
    ans = ''
    while a:
        ans += alph[a%q]
        a //= q
    return ans[::-1]

n = 3 * 15**1140 + 2 * 15**1025 + 15**923 - 3 * 15**85 + 2 * 15 ** 74 + 3
n = toq(n, 15)

c = 1
ans = []
for i in range(len(n) - 1):
    if n[i] == n[i+1]: c += 1
    else:
        ans.append(c)
        c = 1

print(max(ans))