from string import digits, ascii_lowercase

alph = digits+ascii_lowercase
def toq(a, q):
    ans = ''
    while a:
        ans += alph[a%q]
        a//=q
    return ans[::-1]

pattern = "".join([str(i%2==0) for i in range(6)])
count = 0
for i in range(int("10000", 20), int("100000", 20)):
    n = toq(i, 20)
    c1 = "".join([str(int(j,20)%2 == 0) for j in n]) in pattern
    c2 = int(n[0], 20) + int(n[-1], 20) == 26
    if c1 & c2: count+=1

print(count)