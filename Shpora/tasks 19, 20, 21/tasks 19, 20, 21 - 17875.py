def f(a, n):
    if a <= 19: return n % 2 == 0
    if n == 0: return 0
    h = [f(a - 2, n - 1),
         f(a - 5, n - 1),
         f(a // 3, n - 1)]
    return all(h) if n % 2 == 0 else any(h)

print("19)", *[a for a in range(20, 1_000) if f(a, 2)])
print("20)", *[a for a in range(20, 1_000) if f(a, 3) and not f(a, 1)])
print("22)", *[a for a in range(20, 1_000) if f(a, 4) and not f(a, 2)])
