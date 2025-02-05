from itertools import permutations

count = 0
for i in set(permutations("хочу в вуз")):
    s = "".join(i)
    c1 = (s == s.strip())
    c2 = "  " not in s
    s = s.split()
    c3 = all(j[0] != "у" for j in s)
    c4 = len(s) >= 2
    if c1 & c2 & c3 & c4: count += 1
print(count)
