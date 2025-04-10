with open("17_6791.txt") as f:
    data = [int(i) for i in f]

minN = min(i for i in data if str(i)[-2:] == "68") ** 2

ans = []

for n1, n2 in zip(data, data[1:]):
    c1 = (str(n1)[-2:] == "68") ^ (str(n2)[-2:] == "68")
    c2 = n1 ** 2 + n2 ** 2 >= minN
    if c1 and c2: ans.append(n1 ** 2 + n2 ** 2)

print(len(ans), max(ans))
