from itertools import combinations

data = open("24.txt").read()

ans = []
for i in range(100000):
    s = "RSQ" * i
    if s + "RSQ" not in data:
        for j in combinations(["", "Q", "SQ", "RSQ" * i, "RS", "R", ""], 3):
            j = ''.join(j)
            if j in data: ans.append(len(j))
        print(max(ans))
        exit(80085)
