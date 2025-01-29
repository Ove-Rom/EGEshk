from itertools import permutations

graph = "ав аб бв бд вг ге дж гд еж ез жз".split()
matrix = "356 358 128 67 127 147 456 23".split()

print(*range(1, 9))

for i in permutations("абвгдежз"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)