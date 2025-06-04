from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for x in alph[:23]:
    n1 = int(f"7{x}38596", 23)
    n2 = int(f"14{x}36", 23)
    n3 = int(f"61{x}7", 23)
    n = n1 + n2 + n3
    if n % 22 == 0:
        print(n // 22)
        break
