from fnmatch import fnmatch

for i in range(1234, 10**10, 1234)[::-1]:
    if fnmatch(str(i), "4*5*6") and fnmatch(str(i), "?74*68?"):
        print(i, i//1234)