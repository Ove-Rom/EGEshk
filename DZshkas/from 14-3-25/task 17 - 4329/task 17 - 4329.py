with open("17_4329.txt") as f:
    data = [int(i) for i in f]

def div(x):
    ans = set()
    for i in range(1, round(x ** .5) + 1):
        if x % i == 0:
            ans |= {i, x // i}
    return ans

maxN = max([div(i) for i in data], key=len)

ans = []

for n1, n2 in zip(data, data[1:]):
    d1 = div(n1)
    d2 = div(n2)
    i1 = maxN.intersection(d1)
    i2 = maxN.intersection(d2)
    if len(i1) >= 3 and len(i2) >= 3:
        ans.append(len(d1.intersection(d2)))

print(len(ans), max(ans))