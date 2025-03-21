from string import digits, ascii_lowercase

for x in (digits+ascii_lowercase)[24::-1]:
    n1 = int(f"a4{x}7f2", 25)
    n2 = int(f"n{x}g5{x}h", 25)
    n3 = int(f"74{x}m26", 25)
    n = n1 + n2 + n3
    if n % 24 == 0:
        print(n // 24); break
