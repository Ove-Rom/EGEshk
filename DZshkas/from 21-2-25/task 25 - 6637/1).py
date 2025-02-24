from fnmatch import fnmatch

for i in range(1021394 + -1021394 % 3052, 10 ** 10, 3052):
    if fnmatch(str(i), "1?2139*4"):
        print(i, i // 3052)