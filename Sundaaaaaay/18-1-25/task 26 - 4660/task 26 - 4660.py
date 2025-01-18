with open("26_4660.txt") as file:
    file.readline()
    data = [int(i) for i in file]

data = sorted(data, reverse=True)

deshovoye = data[len(data) // 4 * 3:]
dorogoye = data[:len(data) // 4 * 3]

bestie = []
nePoSkidke = []

for i in range(len(data)):
    if (i + 1) % 4 == 0:
        bestie.append(data[i])
    else:
        nePoSkidke.append(data[i])

summOne = sum(dorogoye) + sum(deshovoye) // 2
summChelKapetsTiUmni = sum(nePoSkidke) + sum(bestie) // 2

print(summChelKapetsTiUmni, summOne)
