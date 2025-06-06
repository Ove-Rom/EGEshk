with open("26_17687.txt") as f:
    n = int(f.readline())
    data = [int(i) for i in f]

data = sorted(data, reverse=True)
chel = sum(data) - sum(data[:len(data)//9])

# data = sorted(data)
shop = sum(data) - sum(data[8::9])

print(chel, shop)
