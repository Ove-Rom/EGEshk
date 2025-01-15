from itertools import permutations

graph = "ab ac ad bc cd ce de df ef eg fg".split()
matrix = "34 3456 1245 1237 236 25 14".split()

print(*range(1, 8))

for i in permutations("abcdefg"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
