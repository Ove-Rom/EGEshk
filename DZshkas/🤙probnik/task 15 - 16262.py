from tqdm import tqdm

c = 0

for a in tqdm(range(-1000, 1000)):
    if all(((a < x) or
            (x ** 2 - 7 * x + 10 > 0)) and
           ((a >= y) or (y ** 2 +7 * y + 12 > 0))
           for x in range(-1000, 1000)
           for y in range(-1000, 1000)):
        c += 1

print(c)
