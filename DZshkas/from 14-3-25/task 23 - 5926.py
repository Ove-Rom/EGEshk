ans = set()

def f(a, c = 0, d = None):
    if c == 24:
        ans.add(a)
        return 0
    match d:
        case 'a': return f(a + 7, c + 1, 'b'), f(a * 4, c + 1, 'c')
        case 'b': return f(a + 1, c + 1, 'a'), f(a * 4, c + 1, 'c')
        case 'c': return f(a + 1, c + 1, 'a'), f(a + 7, c + 1, 'b')
        case _: return f(a + 1, c + 1, 'a'), f(a + 7, c + 1, 'b'), f(a * 4, c + 1, 'c')

f(1)

print(len(ans))