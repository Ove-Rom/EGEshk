with open("task 9 - 21704.txt") as f:
    data = [list(map(int, i.split())) for i in f]

for l in data:
    c1 = l == sorted(l, reverse=True)
    s = min(l) + max(l)
    c2 = (sum(l) - s) / 5 < s / 2
    if c1 and c2:
        print(sum(l))
        break