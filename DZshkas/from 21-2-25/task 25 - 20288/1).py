from fnmatch import fnmatch

for i in range(12141 + -12141 % 9231, 10**10, 9231):
    if fnmatch(str(i), "*12[13579]4[13579]") and all(int(i) % 2 == 0 for i in str(i)[:-5]):
        print(i, i//9231)