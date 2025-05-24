from collections import Counter
from string import ascii_uppercase

with open("24-164.txt") as f:
    data = f.readlines()

ans = Counter()

for line in data:
    count = Counter()
    line = line.replace("X", "X ")
    for i in line.split()[1:]:
        count[i[0]] += 1
    mx = count.most_common()[0][1]
    n = 0
    while count.most_common()[n][1] == mx:
        ans[count.most_common()[n][0]] += 1
        n += 1

print(ans.most_common()[0][1])
