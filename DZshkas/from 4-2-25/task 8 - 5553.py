from itertools import permutations

count = 0

for i in set(permutations("соточка")):
    s = "".join(i)
    for j in "оа":
        s = s.replace(j, "x")
    if "xx" in s:
        count += 1
print(count)