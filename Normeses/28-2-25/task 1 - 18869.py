from itertools import permutations

graph = "ab bc cd de eh ha ga gf gh fc fe".split()
matrix = "568 36 247 368 178 124 35 845".split()

print(*range(1,9))

for i in permutations("abcdefgh"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)