with open("26_4604.txt") as f:
    data = [int(i) for i in f]

data = sorted(data, reverse=True)

curBox = float("inf")
count = 0

for box in data:
    if curBox - box >= 3:
        curBox = box
        count += 1

print(count, curBox)