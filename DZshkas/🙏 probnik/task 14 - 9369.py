from string import digits, ascii_lowercase

alph = digits + ascii_lowercase
ans = []

for x in alph[:16]:
    for y in alph[:16]:
        n1 = int(f"27a{x}23", 16)
        n2 = int(f"8{y}e5d2", 16)
        n = n1 + n2
        if n % 5 == 0:
            ans.append(int(x, 16) + int(y, 16))

print(max(ans))