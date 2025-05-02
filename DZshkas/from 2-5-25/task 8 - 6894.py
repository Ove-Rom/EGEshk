from itertools import product

for n, i in enumerate(product(sorted("цапля"), repeat=5), start=1):
    c1 = i.count("а") <= 1
    c2 = i.count("ц") == 2
    c3 = i.count("л") == 0
    if c1 and c2 and c3:
        print(n)
        break
