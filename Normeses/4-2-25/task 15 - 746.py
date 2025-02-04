from itertools import combinations

def f(x):
    p = 12 <= x <= 26
    q = 30 <= x <= 53
    a = a1 <= x <= a2
    return (a <= p) or q

ans = []
line = [0, 12, 26, 30, 53, 60]

for a1, a2 in combinations(line, 2):
    if all(f(x/10) for x in range(a1*10-1, a2*10+1)):
        ans.append(a2-a1)

print(max(ans))