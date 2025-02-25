from fnmatch import fnmatch

c = 0
ans = []

for i in range(10 ** 10 - 10**10 % 53191, 2136 + -2136 % 53191, -53191):
    # print(i, i / 53191)
    if fnmatch(str(i), "[2468]136*[13579]"):
        ans.append((i, i // 53191))
        c += 1
        if c == 5: break

for i in ans[::-1]:
    print(*i)