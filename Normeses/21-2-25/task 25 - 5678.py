from itertools import product
ans = []
for i in range(4):
    for j in range(4):
        if i + j <= 2:
            for f in product("1234567890", repeat=i):
                for s in product("1234567890", repeat=j):
                    f = ''.join(f)
                    s = ''.join(s)
                    st = f"124{f}5{s}79"
                    summ = sum(int(num) for num in st if int(num)%2 != 0)
                    if int(st) % summ ==0:  ans.append([int(st), sum(int(num) for num in st)])

for i in sorted(ans):
    print(*i)