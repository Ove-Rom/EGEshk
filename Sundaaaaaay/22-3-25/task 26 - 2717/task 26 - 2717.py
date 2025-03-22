from itertools import groupby
from re import search

with open("26_2717.txt") as f:
# with open("test") as f:
    n = f.readline()
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)

pattern = r"10*000+1"

for row, places in groupby(data, lambda x: x[0]):
    places = list(places)
    if len(places) >= 5:
        line = ['0']*max(int(j) for i, j in places)
        for i, j in places:
            line[j-1] = '1'
        line = ''.join(line)
        result = search(pattern, line)
        if not result:
            print(row, max(places, key=lambda x: x[1])[1])
            break