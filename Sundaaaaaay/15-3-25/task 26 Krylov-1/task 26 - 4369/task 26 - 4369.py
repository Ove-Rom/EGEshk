with open("26_4369.txt") as f:
    # with open("test") as f:
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

d0 = 500
d1 = 100

h = max(data)[0]
v = max(data, key=lambda x: x[1])[1]

base = []

for i in range(h):
    base.append(['x'] * v)

for i in data:
    base[i[0] - 1][i[1] - 1] = i[2]
ans = []

for i in range(len(base)):
    l = 0
    if base[i].count(0) >= d0 and f"1{'x' * d1}" in ''.join(str(j) for j in base[i]):
        ans.append([i + 1, base[i].count(1)])
        # lens = sorted(len(list(group)) for letter, group in groupby(base[i]) if letter == 'x')[::-1]
        # print(lens)
        # for len in lens:
        #     if f"1{'x'*len}1" in ''.join(str(j) for j in base[i]):
        #         l = len
ans = sorted(ans)

print(ans[-1][0], ans[-1][1])
