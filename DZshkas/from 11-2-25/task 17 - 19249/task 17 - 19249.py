with open("17_19249.txt") as f: data = [int(i) for i in f]

maxN = max(i for i in data if len(str(abs(i))) == 5 and str(i)[-2:] == "43") ** 2

ans = []

for i in range(len(data) - 2):
    n1, n2, n3 = data[i:i+3]
    c1 = len(str(abs(n1))) == 5 and str(n1)[-2:] == "43"
    c2 = len(str(abs(n2))) == 5 and str(n2)[-2:] == "43"
    c3 = len(str(abs(n3))) == 5 and str(n3)[-2:] == "43"
    if (c1 or c2 or c3) and sum([n1**2, n2**2, n3**2]) <= maxN:
        ans.append(sum([n1**2, n2**2, n3**2]))

print(len(ans), min(ans))