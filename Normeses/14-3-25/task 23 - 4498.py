def f(a, b, c1=0, c2=0, c3=0):
    if a == b:
        if c1 <= 4 and c2 >= 2 and c3 == 5: return 1
        return 0
    if a > b or c3 > 5 or c1 > 4: return 0
    return f(a * 5, b, c1 + 1, c2, c3) + \
        f(a * 3, b, c1, c2 + 1, c3) + \
        f(a + 45, b, c1, c2, c3 + 1)

print(f(1, 2970))