from itertools import product

print(list(''.join(i) for i in product(sorted("школа"), repeat=5)).index("шалаш") + 1)