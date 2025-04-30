def div(x):
    ans = set()
    for i in (1, int(x ** .5) + 1):
        if x % i == 0:
            if str(i)[0] == "4": ans.add(i)
            if str(x//i)[0] == "4": ans.add(x//i)
    if len(ans) == 24: return max(ans)
    return False

for i in range(10**6):
    if d:= div(i):
        print(i, d)
