with open("27A.txt") as fA:
    fA.readline()
    kA = int(fA.readline())
    tA = int(fA.readline())
    dataA = [int(i) for i in fA]

sumA = [sum(dataA[i:i + kA]) for i in range(len(dataA) - kA + 1)]

sumAs = sorted(sumA)

maxA = sumAs.pop(0)

for i in sumAs:
    if abs(sumA.index(maxA) - sumA.index(i)) - kA >= tA:
            print(maxA + i)
            break

# with open("27B.txt") as fB:
#     fB.readline()
#     kB = int(fB.readline())
#     tB = int(fB.readline())
#     dataB = [int(i) for i in fB]
#
# sumB = [sum(dataB[i:i + kB]) for i in range(len(dataB) - kB + 1)]
#
# sumBs = sorted(sumB)
#
# maxB = sumBs.pop(0)
#
# for i in sumBs:
#     if abs(sumB.index(maxB) - sumB.index(i)) - kB >= tB:
#             print(maxB + i)
#             break