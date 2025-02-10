def div(x):
    ans = set()
    for i in range(2, round(x**0.5) + 1):
        if x%i == 0:
            if i % 10 == 7: ans.add(i)
            if (x // i) % 10 == 7: ans.add(x//i)
    return sorted(ans)

count = 0

for i in range(550_001, 10**10):
    divs = div(i)
    if len(divs) == 3:
        print(i, divs[-1])
        count += 1
        if count == 5: break