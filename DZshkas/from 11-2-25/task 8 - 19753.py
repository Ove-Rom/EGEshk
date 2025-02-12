count = 0

for i in range(100000, 1000000, 4):
    s = str(i)
    if len(s) == len(set(s)) and "TrueTrue" not in ''.join(str(int(j) % 2 == 0) for j in s):
        count += 1

print(count)
