with open("task 9 - 20899.txt") as f:
    data = [list(map(int, i.split())) for i in f]

count = 0

for line in data:
    maxN = max(line)
    other = sum(line) - maxN
    c1 = maxN < other
    c2 = len(set(line)) == len(line) - 1
    if c1 and c2:
        count += 1

print(count)