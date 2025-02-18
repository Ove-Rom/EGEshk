from fnmatch import fnmatch

for i in range(121500, 10**8, 2025):
    if fnmatch(str(i), "12*34?5"):
        print(i, i//2025)