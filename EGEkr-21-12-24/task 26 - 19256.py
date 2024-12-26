with open("26_19256.txt") as file:
    file.readline()
    data = file.read().split("\n")

base = dict()

for info in data:
    info = info.split()
    id = int(info[0])
    num = int(info[1])
    if id not in base:
        base[id] = [num]
    else:
        base[id].append(num)

leaderId = 0
leaderNums = 0

for student in base.items():
    student = list(student)
    student[1] = sorted(student[1])
    if all(student[1][j] + 1 == student[1][j+1] for j in range(len(student[1]) - 1)):
        if leaderNums < len(student[1]):
            leaderId = student[0]
            leaderNums = len(student[1])
        elif leaderNums == len(student[1]):
            leaderId = min(leaderId, student[0])

print(leaderId, leaderNums)