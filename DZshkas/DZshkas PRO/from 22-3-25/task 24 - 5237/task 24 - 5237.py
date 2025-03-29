from re import fullmatch

data = open("24_5237.txt").read()

data = data.replace('Z', ' ').split()

# patttern = "XY" * 10**5
#
# print(max(len(i) for i in data if i in patttern))

l = []

for i in data:
    if fullmatch(r"Y?(XY)*X?", i) or \
            fullmatch(r"X?(YX)*Y?", i):
        l.append(i)

print(len(max(l, key=len)))