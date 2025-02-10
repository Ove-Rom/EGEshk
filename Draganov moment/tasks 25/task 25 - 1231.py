def div(x):
    ans = set()
    for i in range(2, round(x ** 0.5)):
        if x % i == 0:
            ans.add(i)
            ans.add(x // i)
    return sorted(ans)

count = 0
ans = dict()
for i in range(250200, 10**10):
    divs = div(i)
    if divs:
        if (divs[0] + divs[-1]) % 123 == 17:
            count += 1
            # ans[i] = divs[0] + divs[-1]
            print(i, divs[0] + divs[-1])
            if count == 5: break

# print(ans)
