ans = 0
for n, i in enumerate(range(10_000, 100_000), start=1):
    s = "".join(str(int(j) % 2) for j in str(i))
    c1 = "00" not in s
    c2 = "11" not in s
    c3 = n % 15 == 0
    if c1 and c2 and c3:
        ans = n

print(ans)