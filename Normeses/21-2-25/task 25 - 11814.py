from fnmatch import fnmatch

for i in range(123000386, 10**10, 1777):
    if fnmatch(str(i), "123???4?5"):
        print(i, i//1777)