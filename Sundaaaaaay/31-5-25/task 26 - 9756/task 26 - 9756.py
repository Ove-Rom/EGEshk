with open("26_9756.txt") as f:
# with open("test") as f:
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: [x[1], -x[0]])
last = 0
true_events = [data[0]]

for event in data:
    if event[0] >= true_events[-1][1]:
        true_events.append(event)

for start, stop in data:
    if start >= true_events[-2][1]:
        last = max(last, stop)

print(len(true_events), last)