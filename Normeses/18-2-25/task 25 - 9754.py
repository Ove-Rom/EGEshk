from fnmatch import fnmatch

for i in range(28322, 10**8, 2023):
    if fnmatch(str(i), "3?1*57"):
        print(i, i//2023)