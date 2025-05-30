with open("26_4205.txt") as f:
# with open("test") as f:
    n = int(f.readline())
    data = dict()
    for i in f:
        line, row = map(int, i.split())
        if line in data:
            data[line].append(row)
        else:
            data[line] = [row]

maxLine = 0
minRows = []

for line in sorted(data.items()):
    row = line[1][0]
    for curRow in sorted(line[1][1:]):
        if curRow - row == 14:
            maxLine = line[0]
            minRows.append([line[0], row+1])
        row = curRow

print(maxLine, max(minRows, key=lambda x: [x[0], -x[1]])[1])