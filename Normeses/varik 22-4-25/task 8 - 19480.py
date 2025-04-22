from itertools import permutations

c = 0

for i in set(permutations("парижанка")):
    s =  "".join(i)
    if sum(j in s for j in ["иа", "аа"]) == 1:
        c += 1

print(c)