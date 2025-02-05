from itertools import permutations

count = 0

for i in set(permutations("sotocka")):
    s = "".join(i)
    for j in "oa":
        s = s.replace(j, "x")
    if "xx" not in s:
        count += 1
print(count)