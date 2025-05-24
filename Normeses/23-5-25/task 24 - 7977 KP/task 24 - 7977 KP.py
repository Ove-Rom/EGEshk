from re import finditer


def m(x):
    s = x.split("+")
    summ = 0
    for i in s:
        mult = 1
        for j in i.split("*"):
            mult *= int(j, 6)
        summ += mult
    return summ


with open("24-314.txt") as f:
    data = f.read()

n = r"([1-5][0-5]*|0)"
pat = rf"({n}[+*])+{n}"
ans = []

for i in finditer(pat, data):
    ans.append(i.group())

print(m(max(ans, key=lambda x: [len(x), m(x)])))
