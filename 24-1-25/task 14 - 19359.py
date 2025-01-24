from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for x in alph[:22][::-1]:
    n1 = int(f"a23{x}ac0", 22)
    n2 = int(f"gb{x}21670", 22)
    n = n1 + n2
    if n % 21:
        print(n / 22)
        break
