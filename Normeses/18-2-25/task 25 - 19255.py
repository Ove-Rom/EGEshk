from fnmatch import fnmatch

for i in range(5401027-13117, 10**10, 18579):
    if fnmatch(str(i), "54?1?3*7"):
        print(i, i//18579)