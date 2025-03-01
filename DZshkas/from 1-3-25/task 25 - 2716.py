def div(x):
    ans = set()
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            if i <= x // 2: ans.add(i)
            if x // i <= x // 2: ans.add(x // i)
    if len(ans) >= 3: return sum(sorted(ans)[-3:])
    return 0


ans = []

for i in range(1_200_000, 0, -1):
    s = div(i)
    if s and s % 2022 == 0 and s != i:
        ans.append([i, s])
        if len(ans) == 5:
            for j in ans[::-1]:
                print(*j)
            break
