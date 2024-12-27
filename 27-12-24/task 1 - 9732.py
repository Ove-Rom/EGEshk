from itertools import permutations

graph = "GA AD DB BE EG BF FE FC CE CG".split()
matrix = "47 357 2567 16 236 345 123".split()
print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)