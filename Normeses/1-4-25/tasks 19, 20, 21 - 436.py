def f(a, b, n):
    if (a + b) >= 44: return n % 2 == 0
    if n == 0: return 0
    h = [f(a + b, b, n - 1),
         f(a, b + a, n - 1)]
    return all(h) if n % 2 == 0 else any(h)

print("20)", *[a for a in range(1, 33) if f(a, 11, 1)])
print("20)", *[a for a in range(1, 33) if f(a, 11, 2)])
print("20)", *[a for a in range(1, 22) if f(a, a, 3)])