with open("24_4544.txt") as f:
    data = f.read()

data = data.split("XIX")

lens = [len(i) + 4 for i in data]

print(max(lens))