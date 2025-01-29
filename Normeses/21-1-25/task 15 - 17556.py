def f(a):
    B = [b for b in range(70, 91)]
    for x in range(1, 1000):
        f1 = (x % a == 0) or (( x in B) <= (x % 22 != 0))
        if not f1: return 0
    else: return 1

for a in range(1000, 0, -1):
    if f(a):
        print(a)
        break