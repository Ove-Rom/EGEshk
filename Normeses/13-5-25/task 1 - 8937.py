from itertools import permutations

graph = "аб бд дг гж жз зе ев ва бв де жд же".split()
matrix = "3578 346 1258 26 13 248 18 1367".split()

print(*range(1, 9))

for i in permutations("абвгдежз"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)