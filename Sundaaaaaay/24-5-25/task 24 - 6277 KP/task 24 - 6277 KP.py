from tqdm import tqdm

with open("24-252.txt") as f:
    data = f.read()

ans = []

for i in tqdm(range(len(data))):
    letter = data[i]
    for j in range(i+1, len(data)):
        if data[j] == letter:
            ans.append([letter, len(data[i:j+1])])
            break

print(*max(ans, key=lambda x: x[1]))