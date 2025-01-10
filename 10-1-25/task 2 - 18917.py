print("t s r a")
for t in 1, 0:
    for s in 1, 0:
        for r in 1, 0:
            for a in 1, 0:
                f = (s or (not r)) and (not (r == a)) and t
                if f:
                    print(t, s, r, a)