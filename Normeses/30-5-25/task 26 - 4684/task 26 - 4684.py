with open('26_4684.txt') as file:
    n = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data)
one = sum(data) - sum(data[:n//6]) // 2

data = sorted(data, reverse=True)
mnogo = sum(data) - sum(data[5::6]) // 2

print(mnogo, one)
