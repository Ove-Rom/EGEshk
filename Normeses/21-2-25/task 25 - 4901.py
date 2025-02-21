from fnmatch import fnmatch

c = 0

for i in range(16464, 10**10, 336):
    if fnmatch(str(i), "?6*6*?6"):
        print(i, i//336)
        c += 1
        if c == 7: break