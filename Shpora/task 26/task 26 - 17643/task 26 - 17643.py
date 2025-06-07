with open("26_17643.txt") as f:
    n = int(f.readline())
    data = dict()
    for i in f:
        art, pr, st = map(int, i.split())
        if art not in data:
            data[art] = [pr, 0, 0] # price, in, out
        data[art][2 - st] += 1

midPrice = sum(i[0] for i in data.values()) / len(data)

leader = max(data.values(), key=lambda x: [x[2], x[0], -x[1]] if x[0] > midPrice else [0])

print(leader[0] * leader[2], leader[1])