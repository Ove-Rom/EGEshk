with open("26_2651.txt") as f:
# with open("test") as f:
    n = f.readline()
    data = [list(map(int, i.split())) for i in f]

base = {}

types = set(range(1, 9))

for year, type in data:
    if year not in base:
        base[year] = types - {type}
    else:
        base[year] -= {type}

s = sum(len(t) for y, t in base.items())
y = max(base.items(), key=lambda x: (len(x[1]), x[0]))

print(s, y[0])