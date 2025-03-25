from functools import reduce

ans = []

for i in range(4, 2_000):
    s = '3' * i + '5'
    while "23" in s or "5333" in s or "33333" in s:
        s = s.replace("23", '3', 1)
        s = s.replace("5333", "32", 1)
        s = s.replace("33333", "55", 1)
    ans.append(sum(int(j) for j in s))

print(min(ans))