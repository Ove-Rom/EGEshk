with open("26_8432.txt") as f:
    f.readline()
    data = [i[:-1] for i in f]

departureCar = []
departureBus = []

car = 70
bus = 30
busCount = 0
sadCount = 0
apertures = dict()

data = sorted(data, key=lambda x: (int(x.split()[0]), (int(x.split()[0]) + int(x.split()[1]))))
for i in data:
    apertures[int(i.split()[0])] = [int(i.split()[0]) + int(i.split()[1]), i.split()[-1]]
maxTime = int(data[-1].split()[0]) + int(data[-1].split()[1])
for curTime in range(maxTime + 1):
    if curTime in departureCar:
        car += 1
    elif curTime in departureBus:
        bus += 1
    if curTime in apertures:
        if apertures[curTime][-1] == 'B':
            if bus > 0:
                bus -= 1
                busCount += 1
                departureBus.append(apertures[curTime][0])
            else:
                sadCount += 1
        else:
            if car > 0:
                car -= 1
                departureCar.append(apertures[curTime][0])
            elif bus > 0:
                bus -= 1
                departureBus.append(apertures[curTime][0])
            else:
                sadCount += 1

print(busCount, sadCount)
