def f(start, stop):
    if start == stop: return 1
    if start == 12: return 0
    if start > stop: return 0
    return f(start + 1, stop) + f(start + 2, stop) + f(start * 3, stop)

print(f(2, 9) * f(9, 19))