from itertools import permutations

count = 0
for i in set(permutations("hocu v vuz")):
    s = "".join(i).split()
    c1 = all(j[0] != "u" for j in s)
    c2 = len(s) >= 2
    if c1 & c2: count += 1
print(count)
