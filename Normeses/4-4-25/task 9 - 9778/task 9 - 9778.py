d = [tuple(map(int, i.split())) for i in open("09_9778.txt")]

for n, i in enumerate(d, start=1):
    np = [j for j in i if i.count(j) == 1]
    p = [j for j in i if i.count(j) != 1]
    c1 = len(p) == 2 and len(set(p)) == 1
    if c1 and p[0] >= sum(np) // 4:
        print(n)
        break