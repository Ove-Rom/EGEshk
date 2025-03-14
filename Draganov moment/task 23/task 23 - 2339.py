ans = set()


def f(a, c=0):
    if c == 15:ans.add(a)
    else:f(a * 2, c + 1), f(a * 2 + 1, c + 1)


f(1)
print(len(ans))
