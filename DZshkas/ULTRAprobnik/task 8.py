from itertools import product

for n, s in enumerate(product(sorted(set("калейдоскоп"), reverse=True), repeat=6)):
    # c1 = n % 2 == 0
    # c2 = s[0] == 'к'
    # c3 = s.count('й') >= 2
    # c4 = s.count('с') == 0
    # c5 = s.count('е') == 0
    # if c1*c2*c3*c4*c5:
    #     print(n)
    #     break
    if n == 243698: print(s)