from fnmatch import fnmatch


def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

for i in range(int("12135664", 7) + -int("12135664", 7) % 333, 10**9, 333):
    n = toq(i, 7)
    if fnmatch(n, "?213*5664"):
        print(i, i // 333)