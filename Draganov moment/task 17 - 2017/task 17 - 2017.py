from string import digits, ascii_lowercase

with open("17_2017.txt") as file:
    data = [int(i) for i in file]

alph = digits + ascii_lowercase

def toq(a, q):
    ans = ''
    while a:
        ans += alph[a%q]
        a //= q
    return ans[::-1]

count = 0
summ = 0

for i in data:
    c1 = toq(i, 16)[-1] == 'b'
    c2 = i % 7 == 0
    c3 = i % 6 != 0
    c4 = i % 13 != 0
    c5 = i % 19 != 0
    if c1 and c2 and c3 and c4 and c5:
        count += 1
        summ += i

print(summ, count)