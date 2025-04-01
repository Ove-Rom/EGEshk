def f(a, n):
    if a >= 36:
        if a <= 85: return n % 2 == 0
        return n % 2
    if n == 0: return 0
    h = [f(a + 2, n - 1),
         f(a * 3, n - 1)]
    return all(h) if n % 2 == 0 else any(h)

print("19)", *[n for n in range(1, 10) if f(30, n)])
print("19)", *[n for n in range(1, 10) if f(32, n)])
print("20)", *[n for n in range(1, 10) if f(8, n)])
print("20)", *[n for n in range(1, 10) if f(10, n)])
print("21)", *[n for n in range(1, 10) if f(6, n)])