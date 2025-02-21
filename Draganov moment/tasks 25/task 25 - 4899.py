def div(x):
    ans = set()
    for i in range(1, round(x ** 0.5) + 1):
        if x % i == 0 == i % 2:
            ans.add(i)
        if (x // i) % 2 == 0 == x // i:
            ans.add(x // i)
    if ans: return ans
    return 0


from fnmatch import fnmatch

c = 0
for i in range(65000, 10**10):
    if fnmatch(str(i), "6*97*5?"):
        if i % 2 == 0:
            x = div(i)
            if len(x) >= 4:
                print(i, sum(x))
                c += 1
                if c == 7:
                    break
