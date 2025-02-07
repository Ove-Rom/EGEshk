count = 0
for a in range(1, 1001):
    if all(((a, 12 == 0) and (530 % x == 0)) <= ((not a % x == 0) <= (not 170 % x == 0)) for x in range(1, 1000)):
        count += 1
print(count)