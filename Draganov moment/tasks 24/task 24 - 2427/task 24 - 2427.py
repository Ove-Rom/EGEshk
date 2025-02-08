data = open("24_2427.txt").read()

ans = []
l = data[0]

for i in range(1, len(data)):
    if data[i-1] > data[i]:
        l+=data[i]
    else:
        ans.append(l)
        l = []

print(*max(ans, key=len))