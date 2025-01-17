from itertools import permutations

graph = "ag af fg gd fh de he db bc be hc".split()
matrix = "234 157 147 138 268 58 23 456".split()

print(*range(1, 9))

for i in permutations("abcdefgh"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)