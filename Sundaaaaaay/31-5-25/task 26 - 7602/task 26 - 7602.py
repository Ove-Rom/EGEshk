with open("26_7602.txt") as f:
    k = int(f.readline())
    n = int(f.readline())
    data = sorted(list(map(int, i.split())) for i in f)

cels = [0] * k
lastCell = 0
count = 0

for input, output in data:
    for i in range(len(cels)):
        if input > cels[i]:
            cels[i] = output
            lastCell = i + 1
            count += 1
            break

print(count, lastCell)
