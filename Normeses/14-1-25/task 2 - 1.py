print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x <= y) * (z == (w <= x)) * (not w)
                if F:
                    print(x, y, z, w)
