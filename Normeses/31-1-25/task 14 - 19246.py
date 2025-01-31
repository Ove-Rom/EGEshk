from string import digits, ascii_lowercase

alph = digits + ascii_lowercase


def toq(a, q):
    ans = ''
    while a:
        ans += alph[a % q]
        a //= q
    return ans[::-1]


for x in alph[:25][::-1]:
    n1 = int(f"11353{x}12", 25)
    n2 = int(f"135{x}21", 25)
    num = n1 + n2
    if num % 24 == 0:
        print(num // 24)
        break
