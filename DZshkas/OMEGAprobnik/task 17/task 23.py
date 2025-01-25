def f(start, stop):
    if start == stop: return 1
    if start > stop: return 0
    if start < stop:
        maxx = max(int(i) for i in str(start))
        return f(start + 2, stop) + f(start + maxx, stop)

print(f(32, 55)+f(55, 76))