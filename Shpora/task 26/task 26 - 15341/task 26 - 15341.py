with open("26_15341.txt") as f:
    n = int(f.readline())
    data = [int(i) for i in f]

data = sorted(data, reverse=True)

curСake = float("inf")
count = 0

for cake in data:
    if curСake - cake >= 8:
        curСake = cake
        count += 1

print(count, curСake)