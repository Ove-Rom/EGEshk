c = 0

for n in range(10**3):
    r = f"{n:x}"
    if r.count("b") % 2 == 0:
        r = "1" + r
    else:
        r += "1"
    r = int(r, 16)
    if 10 <= r <= 99:
        c += 1

print(c)