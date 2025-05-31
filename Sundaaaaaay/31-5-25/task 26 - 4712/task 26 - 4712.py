with open("26_4712.txt") as f:
    n = f.readline()
    data = sorted((int(i) for i in f), reverse=True)

c = 0
curBox = float("inf")

for box in data:
    if curBox - box >= 3:
        c += 1
        curBox = box

print(c, curBox)