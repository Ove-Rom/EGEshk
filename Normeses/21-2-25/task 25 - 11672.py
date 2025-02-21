from fnmatch import fnmatch


for i in range(126150, 10**10, 21025):
    chnch = [str(int(j) % 2) for j in str(i)]
    if chnch.count('1') == chnch.count('0') and fnmatch(str(i), "12*34?5"):
        print(i, i//21025)