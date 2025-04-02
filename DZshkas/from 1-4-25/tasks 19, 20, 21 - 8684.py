def f(n, a, b=19):
    if (a + b) >= 175: return n % 2 == 0
    if n == 0: return 0
    h = [f(n - 1, a + 1, b), f(n - 1, a, b + 1),
         f(n - 1, a * 3, b), f(n - 1, a, b * 3)]
    return all(h) if n % 2 == 0 else any(h)

def f19(n, a, b=19):
    if (a + b) >= 175: return n % 2 == 0
    if n == 0: return 0
    h = [f19(n - 1, a + 1, b), f19(n - 1, a, b + 1),
         f19(n - 1, a * 3, b), f19(n - 1, a, b * 3)]
    return any(h)

print("19)", *[a for a in range(1, 155) if f19(2, a)])
print("20)", *[a for a in range(1, 155) if f(3, a) and not f(1, a)])
print("21)", *[a for a in range(1, 155) if f(4, a) and not f(2, a)])