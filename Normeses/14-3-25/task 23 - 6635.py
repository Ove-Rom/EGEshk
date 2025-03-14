ans = set()

def f(a, c = 0):
    if c == 13:
        if a < 0: ans.add(a)
    else: f(a - 3, c + 1), f(a * -3, c + 1)

f(333)

print(len(ans))