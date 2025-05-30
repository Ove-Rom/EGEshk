with open("26_4629.txt") as f:
    n = int(f.readline())
    data = [int(i) for i in f]

data = sorted(data)
shop = sum(data) - sum(data[:n//4]) // 2

data = sorted(data, reverse=True)
chel = sum(data) - sum(data[:n//4]) // 2

print(chel, shop)