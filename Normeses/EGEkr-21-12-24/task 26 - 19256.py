with open("26_19256.txt") as file:
    file.readline()
    data = file.read().split("\n")
# boxes = ((50, 125), (50, 127), (50, 126), (50, 72), (50, 126), (40, 3), (60, 33), (60, 33), (40, 4))
base = dict()

for info in data:
    info = info.split()
    id = int(info[0])
    num = str(info[1])
    if id not in base:
        base[id] = [num]
    else:
        base[id].append(num)
print(len(sorted(base[40031], key = int)))
nums = " ".join([str(i) for i in range(1, 100001)])
leaderId = 0
leaderNums = 0

for student in base.items():
    student = list(student)
    allCompleted = list(sorted(set(student[1]), key=int))
    learned = []
    count = 0

    for i in range(len(allCompleted)):
        for j in range(i, len(allCompleted)):
            if ' ' + ' '.join(allCompleted[i:j + 1]) + ' ' in nums:
                # print(' '.join(allCompleted[box:st + 1]))
                learned.append(j - i + 1)
    count = max(learned)

    if leaderNums < count:
        leaderNums = count
        leaderId = student[0]
    elif leaderNums == count:
        if leaderId > student[0]:
            leaderId = student[0]

print(leaderId, leaderNums)
