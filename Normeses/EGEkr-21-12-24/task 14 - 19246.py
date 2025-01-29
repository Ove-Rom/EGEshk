from string import digits, ascii_uppercase
alph = digits+ascii_uppercase

for x in alph[:25][::-1]:
    n1 = int(f"11353{x}12", 25)
    n2 = int(f"135{x}21", 25)
    if (n1 + n2) % 24 == 0:
        print((n1 + n2) / 24)
        break