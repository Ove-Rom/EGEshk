from itertools import permutations

count = 0

for i in permutations("хочунабюджет"):
    s = "".join(i)
    for j in "оуаюе":
        s = s.replace(j, "x")
    if "xxxxx" not in s:
        count += 1
print(count)
