with open("26_1379.txt") as f:
    s, n = map(int, f.readline().split())
    data = [int(i) for i in f]

data = sorted(data)

curM = 0
c = 0
for i in range(len(data)):
    if curM + data[i] <= s:
        curM += data[i]
        c += 1
    else:
        data = data[i:]
        break

ans = []

for i in range(len(data) // 2):
    ans.append(data[i] + data[-(i + 1)])

print(c, max(ans))
