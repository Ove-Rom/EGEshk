from itertools import permutations

graph = "AF AB AE FC CH CG GD DH HB BE".split()
matrix = "28 157 456 136 23 34 28 17".split()

print(*range(1, 9))
for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)