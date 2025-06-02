from itertools import permutations

graph = "ef fd dc ca ag gb be fc ab".split()
matrix = "246 26 57 15 347 127 356".split()

print(*range(1, 8))

for i in permutations("abcdefg"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)