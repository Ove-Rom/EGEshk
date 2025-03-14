a = [1] + [0] * 100

for i in range(1, 100):
    a[i] = a[i - 5] + a[i - 4] + a[i - 2]
    if a[i] == 1001:
        print(31 + i)
        break