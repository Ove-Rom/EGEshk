ans = []

for n in range(1, 100):
    r = f"{n:b}"
    r += str(r.count("1") % 2)
    r += str(r.count("1") % 2)
    r = int(r, 2)
    if r > 75:
        ans.append(r)

print(min(ans))