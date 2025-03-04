with open("26_2614.txt") as f:
    s, n = map(int, f.readline().split())
    data = [int(i) for i in f]

exp = sorted([i for i in data if i > 3000])
enc = sorted([i for i in data if 3000 >= i >= 2000])
com = sorted([i for i in data if i < 2000])

money = s
ans = []

money -= exp[0] + exp[-1] + sum(enc)
count = 2 + len(enc)

for i in com:
    if money - i >= 0:
        money -= i
        count += 1
        ans.append(i)
    else:
        print(count, ans[-1])
        break