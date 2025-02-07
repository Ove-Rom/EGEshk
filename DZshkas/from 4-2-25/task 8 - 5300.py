from itertools import permutations

count = 0
for i in set(permutations("хочу в вуз")):
    s = "".join(i)
    c1 = (s == s.strip())
    c2 = "  " not in s
    x = s.split()
    c3 = all(j[0] != "у" for j in x)
    c4 = len(x) >= 2
    if c1 & c2 & c3 & c4 and s != "хочу в вуз": count += 1
print(count)
