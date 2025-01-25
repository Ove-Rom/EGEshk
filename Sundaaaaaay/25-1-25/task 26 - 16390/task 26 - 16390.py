with open("26_16390.txt") as f:
    s = int(f.readline().split()[0])
    boxes = [int(i) for i in f]

boxes = sorted(boxes)

count = 0
mass = 0
lbox = 0
for box in boxes:
    if mass + box <= s:
        count += 1
        mass += box
        lbox = box

mass -= lbox

for j in boxes[::-1]:
    if mass + j <= s:
        lbox = j
        break
print(count, lbox)
