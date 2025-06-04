with open("task 9 - 17628.txt") as f:
    data = [list(map(int, i.split())) for i in f]

c = 0

for line in data:
    m = max(line)
    n = min(line)
    if m + n <= sum(line) - m - n:
        c += 1

print(c)