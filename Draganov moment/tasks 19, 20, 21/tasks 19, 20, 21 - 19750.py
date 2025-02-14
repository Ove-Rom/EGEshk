def f(s, n):
    if s <= 19: return n % 2 == 0
    if n == 0: return 0
    h = []
    if s >= 5: h.append(f(s - 5, n - 1))
    if s % 2 == 0 and s != 0: h.append(f(s // 2, n - 1))
    if s % 3 == 0 and s != 0: h.append(f(s // 3, n - 1))
    if s % 3 and s % 2: h.append(f(s + 1, n - 1))
    return all(h) if n % 2 == 0 else any(h)

print("19)", *[s for s in range(20, 1900) if f(s, 2) and not f(s, 0)])
print("20)", *[s for s in range(20, 1900) if f(s, 3) and not f(s, 1)])
print("11)", *[s for s in range(20, 1900) if f(s, 4) and not f(s, 2)])
