from fnmatch import fnmatch

for i in range(2023, 10**9, 2023):
    st = str(i)
    s = sum(int(j) for j in st)
    if s % 7 == 0 and s < 20 and fnmatch(st, "20*23"):
        print(i)