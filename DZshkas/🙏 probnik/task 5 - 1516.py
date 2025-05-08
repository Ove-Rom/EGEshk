ans = set()

for n in range(100, 1001):
    r = f"{n:b}"
    r = "1"*r.count("1")
    r = int(r, 2)
    ans.add(r)

print(len(ans))