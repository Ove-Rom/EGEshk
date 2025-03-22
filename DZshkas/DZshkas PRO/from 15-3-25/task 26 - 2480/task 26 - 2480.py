roadToRepair = set()

with open("26_2480.txt") as f:
    # with open("test") as f:
    n = int(f.readline())
    for i in f:
        roadToRepair.update(set(range(int(i.split()[0]), int(i.split()[1]) + 1)))

road = set(range(list(roadToRepair)[-1] + 2))

goodRoad = list(road - roadToRepair)
ans = []

for i in range(len(goodRoad) - 1):
    if goodRoad[i + 1] - goodRoad[i] != 1:
        ans.append(goodRoad[i + 1] - goodRoad[i] - 2)

print(len(ans), sum(ans))
