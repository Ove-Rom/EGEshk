with open("26_2480.txt") as f:
    # with open("test") as f:
    n = int(f.readline())
    data = [set(range(list(map(int, i.split()))[0], list(map(int, i.split()))[1] + 1)) for i in f]

roadToRepair = set()

for i in data:
    roadToRepair.update(i)

road = set(range(list(roadToRepair)[-1] + 2))

goodRoad = list(road - roadToRepair)
ans = []

for i in range(len(goodRoad) - 1):
    if goodRoad[i + 1] - goodRoad[i] != 1:
        ans.append(goodRoad[i + 1] - goodRoad[i] - 2)

print(len(ans), sum(ans))
