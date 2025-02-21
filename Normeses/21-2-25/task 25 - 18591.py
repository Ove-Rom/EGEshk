from fnmatch import fnmatch

for i in range(1902300864, 10**10, 1984):
    s = str(i)
    if fnmatch(s, "[13579]9?23?*23[13579][02468]"):
            print(i, i//1984)