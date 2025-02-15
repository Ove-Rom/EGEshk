from string import digits, ascii_lowercase

alph = digits + ascii_lowercase


def toq(a, q):
    ans = ''
    while a:
        ans += alph[a % q]
        a //= q
    return ans[::-1]


n = 3 * 3125 ** 9 \
    + 2 * 625 ** 8 \
    - 4 * 625 ** 7 \
    + 3 * 125 ** 6 \
    - 2 * 25 ** 5 \
    - 2024

print(toq(n, 25).count('0'))
