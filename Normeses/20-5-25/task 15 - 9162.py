def p(a, b, c):
    return a*b > c

def f(x, y ,a):
    return (not p(x, y, a+13)) <= (p(28, y, 520) or p(x, 25, 800))

for a in range(10000, -10000, -1):
    if all(f(x, y, a) for x in range(100) for y in range(100)):
        print(a)
        break