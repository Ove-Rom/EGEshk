def f(a, n, c = None):
    if a > 40: return n % 2 == 0
    if n == 0: return 0
    match c:
        case 3:
            h = [f(a + 6, n - 1, 6),
                 f(a * 2, n - 1, 2)]
        case 6:
            h = [f(a + 3, n - 1, 3),
                 f(a * 2, n - 1, 2)]
        case 2:
            h = [f(a + 3, n - 1, 3),
                 f(a + 6, n - 1, 6)]
        case _:
            h = [f(a + 3, n - 1, 3),
                 f(a + 6, n - 1, 6),
                 f(a * 2, n - 1, 2)]
    return all(h) if n % 2 ==0 else any(h)

print("19)", *[a for a in range(2, 37) if f(a, 2)])
print("20)", *[a for a in range(2, 37) if f(a, 3) and not f(a, 1)])
print("21)", *[a for a in range(2, 37) if f(a, 4) and not f(a, 2)])
