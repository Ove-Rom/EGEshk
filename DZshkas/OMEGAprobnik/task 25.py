ans = []
for i in range(65000, 10000000000000000):
    if len(ans) == 7: break
    st = str(i)
    c1 = st[0] == '6'
    c2 = '97' in st
    c3 = st[-2] == '5'
    if c1 & c2 & c3:
        dell = [j for j in range(2, i + 1, 2) if i % j == 0]
        if len(dell) >= 4:
            ans.append(str(i) + ' ' + str(sum(dell)))

print(*ans)
