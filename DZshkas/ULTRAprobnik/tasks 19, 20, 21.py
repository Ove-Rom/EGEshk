def f(a, b, n):
    if a * b >= 777: return n % 2 == 0
    if n == 0: return 0
    h = [f(a + 3, b, n - 1), f(a, b + 3, n - 1),
         f(a * 3, b, n - 1), f(a, b * 3, n - 1)]
    return all(h) if n % 2 == 0 else any(h)

def f19(a, b, n):
    if a * b >= 777: return n % 2 == 0
    if n == 0: return 0
    h = [f(a + 3, b, n - 1), f(a, b + 3, n - 1),
         f(a * 3, b, n - 1), f(a, b * 3, n - 1)]
    return any(h)

print("19)", *[s for s in range(1, 111) if f19(7, s, 2)])
print("20)", *[s for s in range(1, 111) if f(7, s, 3)and not f(7, s, 1)] )
print("21)", *[s for s in range(1, 111) if f(7, s, 4) and not f(7, s, 2)] )