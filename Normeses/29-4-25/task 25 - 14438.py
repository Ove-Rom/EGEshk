from fnmatch import fnmatch

sq = [i ** 2 for i in range(500)]

for i in range(1746008 + 1746008 % 86513, 10**12, 86513):
    if fnmatch(str(i), "17*46??8"):
        s = sum(int(j) for j in str(i))
        if s in sq:
            print(i, s)