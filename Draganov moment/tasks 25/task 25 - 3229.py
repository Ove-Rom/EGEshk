from fnmatch import fnmatch

for i in range(123450600, 10**9, 17):
    if fnmatch(str(i), "12345?6?8"):
        print(i, i // 17)