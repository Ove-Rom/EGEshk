ans = []
for n in range(1, 1000):
    r = f"{n:b}"
    if n % 3 == 0:
        r += r[-1] * 3
    else:
        r += bin(n % 3 * 3)[2:]
    r = int(r, 2)
    if r <= 170:
        ans.append(r)

print(min(ans))