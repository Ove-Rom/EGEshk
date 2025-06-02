from itertools import permutations

graph = "ce eg gf fa ac cd dh he ab bf".split()
matrix = "68 27 45 237 368 15 248 157".split()

print(*range(1, 9))

for i in permutations("abcdefgh"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)