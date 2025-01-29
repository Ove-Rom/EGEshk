with open("24_19254.txt") as file:
    data = file.read().replace("FSRQ", "FSRQ ").split()

print(max(sum(len(data[j]) for j in range(i, i + 81)) for i in range(len(data) - 80)))