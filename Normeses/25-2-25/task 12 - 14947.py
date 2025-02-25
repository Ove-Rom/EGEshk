ans = []

for n in range(9999, 3, -1):
    s = '1' + '9' * n
    while "19" in s or "49" in s or "999" in s:
        s = s.replace("19", '9', 1)
        s = s.replace("49", "91", 1)
        s = s.replace("999", '4', 1)
    ans.append(sum(int(i) for i in s))

print(max(ans))