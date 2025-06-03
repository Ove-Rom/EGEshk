with open("task 9 - 21704.txt") as f:
    data = [list(map(int, i.split())) for i in f]

for line in data:
    c1 = line == sorted(line, reverse=True)
    minN = min(line)
    maxN = max(line)
    other = sum(line) - maxN - minN
    c2 = (minN + maxN) / 2 > other / 5
    print(c1, c2)
    if c1 and c2:
        print(sum(line))
        break









