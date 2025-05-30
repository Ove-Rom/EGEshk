with open("26_2944.txt") as f:
    s, k = map(int, f.readline().split())
    data = [int(i) for i in f]

data = sorted(data)

fitting = []

for i in data:
    if i <= s:
        s -= i
        fitting.append(i)
    else:
        s += fitting.pop()
        for i in data[::-1]:
            if i <= s:
                s -= i
                fitting.append(i)
                break


print(len(fitting), max(fitting))