from fnmatch import fnmatch

for i in range(1235559, 10**9, 169):
    if fnmatch(str(i), "123*567?"):
        print(i, i // 169)