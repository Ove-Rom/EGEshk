from tqdm import tqdm

with open("24-252.txt") as f:
    data = f.read()

ans = []

for i in tqdm(range(len(data))):
    nxt = data.find(data[i], i+1)
    ans.append([data[i], nxt-i+1])

print(*max(ans, key=lambda x: x[1]))