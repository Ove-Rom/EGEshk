from itertools import permutations

graph = "аб бв вг гд де еб бж жа бд вд".split()
matrix = "346 45 16 12567 24 1347 46".split()

print(*range(1, 8))

for i in permutations("абвгдеж"):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)