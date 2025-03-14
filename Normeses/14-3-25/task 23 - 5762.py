pattern = [i**2 for i in range(10)]

ans = [0] * 100

def f(a, b, c):
    if a == b: ans[c+1] += 1
    if a > b: return 0
    if a in pattern: c += 1; a -= 1
    return f(a + 2, b, c) + f(a + 3, b, c) + f(a * 3, b, c)

f(5, 50, 0)
print(max(ans[1:]))
