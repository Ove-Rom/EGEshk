from itertools import permutations

c = 0

for i in set(permutations("парижанка")):
    if sum(j in "".join(i) for j in ["иа", "аа"]) == 1:
        c += 1

print(c)