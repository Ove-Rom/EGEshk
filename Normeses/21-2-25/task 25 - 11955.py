from fnmatch import fnmatch

for i in range(1021706, 10 ** 10, 133):
    s = str(i)
    c1 = int(s[1]) % 2 == 0
    c2 = all(int(j) % 2 != 0 for j in s[6:-1])
    if c1 and c2 and fnmatch(s, "1?2157*4"):
        print(i, i // 133)
