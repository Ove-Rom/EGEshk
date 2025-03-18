data = []

for x in range(2, 100):
    if not [i for i in range(2, round(x ** .5) + 1) if x % i == 0]:
        data.append(x)

for i in data:
    n = i - 75
    if n > 0 and n % 4 == 0:
        print(n)