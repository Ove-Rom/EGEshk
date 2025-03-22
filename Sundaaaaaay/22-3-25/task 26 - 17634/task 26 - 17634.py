with open("26_17643.txt") as f:
# with open("test") as f:
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

midPrice = sum(j for i, j, k in data) / len(data)

base = dict()

for id, price, stat in data:
    if price > midPrice:
        if id not in base:
            match stat:
                case 1: base[id] = [price, 1, 0]
                case 0: base[id] = [price, 0, 1]
        else:
            match stat:
                case 1: base[id][1] += 1
                case 0: base[id][2] += 1

leader = max(base.items(), key=lambda x: (x[1][2], x[1][0], -x[1][1]))[0]

print(base[leader][0] * base[leader][2], base[leader][1])