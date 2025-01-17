from itertools import permutations

graph = "ba bd bc da dc de df ae cf ge gf".split()
matrix = "23567 145 146 237 127 137 156".split()

print(*range(1, 8))

for i in permutations("abcdefg"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)