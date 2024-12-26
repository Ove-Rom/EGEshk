# with open("26_19256.txt") as file:
#     file.readline()
#     data = file.read().split("\n")
data = ((60, 33), (60, 33), (50, 125), (50, 126), (50, 127), (50, 72), (50, 126))
base = dict()

for info in data:
    # info = info.split()
    id = int(info[0])
    num = int(info[1])
    if id not in base:
        base[id] = [num]
    else:
        base[id].append(num)

nums = [i for i in range(1, 100001)]
leaderId = 0
leaderNums = 0

for student in base.items():
    student = list(student)
    student[1] = list(set(sorted(student[1])))
    if any(student[1][j] + 1 == student[1][j+1] for j in range(len(student[1]) - 1)):
        count = max(j - i + 1 for i in range(len(student[1])) for j in range(i+1, len(student[1])-1) if student[1][i:j+1] in nums)

        if leaderNums < len(student[1]):
            leaderId = student[0]
            leaderNums = len(student[1])
        elif leaderNums == len(student[1]):
            leaderId = min(leaderId, student[0])

print(leaderId, leaderNums)