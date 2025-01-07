from string import digits, ascii_lowercase
alph = digits + ascii_lowercase

def toq(a, q):
    ans = ''
    while a:
        ans += alph[a % q]
        a //= q
    return ans[::-1]

count = 0
for i in range(int('e' * 5, 15), int('e' * 6, 15)):
    i = toq(i, 15)
    c1 = i.count('8') == 1
    c2 = sum(int(j, 15) > 9 for j in i) >= 2
    # print(c1, c2, sum(int(j, 15) > 9 for j in i))
    if c1 & c2:
        count += 1

print(count)