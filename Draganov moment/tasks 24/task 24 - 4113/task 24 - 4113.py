with open("24_4113.txt") as f:
    data = f.read()

ans = []
for i in range(len(data)):
    count = 0
    if data[i:i+2] in ["BB", "DD"]:
        for j in range(i, len(data)-1, 2):
            if data[j:j + 2] in ["BB", "DD"]:
                count+=1
            else:
                ans.append(count)
                break

print(max(ans))

d = [0] * len(data)

for i in range(1, len(data)):
    if data[i - 1:i + 1] in ["BB", "DD"]:
        d[i] = d[i - 2] + 1
print(max(d))
