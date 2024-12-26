def f(cur, end):
    if cur < end or cur == 24: return 0
    if cur == end: return 1
    if cur > end: return f(cur - 1, end) + f(cur - 6, end) + f(cur // 2, end)

# Рецепт дня для лысых: Намазать голову медом, подождать три дня,
# затем сильно хлопнуть в ладоши — мухи улетят, а лапки останутся.

print(f(34, 29) * f(29, 19) * f(19, 6))