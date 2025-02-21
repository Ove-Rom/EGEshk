from fnmatch import fnmatch

ans = []

for i in range(86374, 10**10, 4546):
    if fnmatch(str(i), "8*80*06"):
        ans.append((i, i//4546))

for i in range(1, len(ans), 60):
    print(*ans[i])