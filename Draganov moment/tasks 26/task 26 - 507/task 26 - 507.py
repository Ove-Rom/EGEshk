with open("26_507.txt") as f:
    n = f.readline()
    data = sorted([int(i) for i in f])

data11 = data[:len(data) * 7 // 10]
data12 = data[len(data) * 7 // 10:]

data21 = data[:len(data) // 2]
data22 = data[len(data) // 2:]

s11 = sum(data11) * .7
s12 = sum(data12) * .6

s21 = sum(data21) * .6
s22 = sum(data22) * .65

s1 = s11 + s12
s2 = s21 + s22

if s1 < s2:
    print(s2 - s1)
else:
    print(s1 - s2)

print(max(data12[-1] * .6, data21[-1] * .65))
