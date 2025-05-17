with open("26_3088.txt") as f:
    n = f.readline()
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)

timeline = [0] * 961
prepearing = []
times = dict()
cookingTime = {i: [] for i in range(1000)}

for t, i in data:
    if i not in prepearing:
        prepearing.append(i)
        times[i] = t
    else:
        prepearing.remove(i)
        cookingTime[i].append(t - times[i])
        timeline[t] += 1

ordersIn1Hour = 0
for i in range(961):
    ordersIn1Hour = max(ordersIn1Hour, sum(timeline[i:i + 60]))

midTime = max(cookingTime.items(), key=lambda x: sum(x[1]) / len(x[1]) if x[1] else 0)[0]

print(ordersIn1Hour, midTime)
