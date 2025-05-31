with open("26_6031.txt") as f:
    n = f.readline()
    data = sorted((int(i) for i in f), reverse=True)

c = 0
curRing = float("inf")

for ring in data:
    if curRing - ring >= 6:
        c += 1
        curRing = ring

print(c, curRing)