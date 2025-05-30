with open("26_4660.txt") as f:
    n = int(f.readline())
    data = [int(i) for i in f]

data = sorted(data)
one = sum(data) - sum(data[:n//4]) // 2

mnogo = sum(data) - sum(data[::4]) // 2

print(mnogo, one)