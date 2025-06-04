from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for x in alph[:21]:
    n1 = int(f"82934{x}2", 21)
    n2 = int(f"2924{x}{x}7", 21)
    n3 = int(f"67564{x}8", 21)
    n = n1 + n2 + n3
    if n % 20 == 0:
        print(n // 20)
        break