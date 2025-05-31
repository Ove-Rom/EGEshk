with open("26_6759.txt") as f:
# with open("test") as f:
    n = int(f.readline())
    data = sorted(int(i) for i in f)
data.reverse()

shop = sum(data) - sum(data[2::3]) // 2

chel = sum(data) - sum(data[:n//3]) // 2

print(chel, shop)
