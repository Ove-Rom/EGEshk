with open("17_2003.txt") as file:
    data = [int(i) for i in file]

count = 0
maxx = 0

for i in data:
    c1 = i % 3 == 0
    c2 = i % 7 != 0
    c3 = i % 17 != 0
    c4 = i % 19 != 0
    c5 = i % 27 != 0
    if c1 and c2 and c3 and c4 and c5:
        count += 1
        maxx = max(maxx, i)

print(count, maxx)
