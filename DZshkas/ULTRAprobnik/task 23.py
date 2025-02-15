def f(start, stop):
    if start in [36, 100]: return 0
    if start < stop: return 0
    if start == stop: return 1
    if start > stop: return f(start // 2, stop) + f(start // 3, stop) + f(start - 3, stop)


print(f(163, 45) * f(45, 3))
