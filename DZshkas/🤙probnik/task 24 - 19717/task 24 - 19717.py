from tqdm import tqdm

with open("24.5_19717.txt") as f:
    data = f.read()

# data = "AAAMAASAMAAAAMAMMAAAAAAAAAAAM"
k = 3

data = data.split("M")

ans = []
c = 0

for i in tqdm(range(len(data) - k)):
    lens = []
    for j in range(k+1):
        print(data[i+j])
        lens.append(len(data[i+j]) + 1)
    s = sum(lens)
    ans.append(s-1)
    print(s-1)

print(max(ans))