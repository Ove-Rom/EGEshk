from itertools import permutations

graph = "аб бд де ез зж жв вг га ад зв гд".split()
matrix = "245 15 478 135 1246 58 38 367".split()

print(*range(1, 9))

for i in permutations("абвгдежз"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)