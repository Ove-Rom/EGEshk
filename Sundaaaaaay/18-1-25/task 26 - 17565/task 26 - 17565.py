# with open("26_17565.txt") as file:
#     file.readline()
#     data = [(int(i.split()[0]), int(i.split()[1]) + int(i.split()[2]) + int(i.split()[3]), int(i.split()[4])) for i in file]
# places = 485
#
# data = sorted(data, key=lambda x: (x[1], x[-1], x[0]), reverse=True)
# print(data)
# summ = 0
# count = 0
#
# for i in data:
#     summ += i[1]
#
# prohodnoy = round(summ / 998, 0)
# print(prohodnoy)
#
# for i in data:
#     if i[1] >= 155:
#         id = i[0]
#         count += 1
#     # else: break
#
# print(id, places - count)

# КомпЕГЭ (17565) от Павла 🍴
with open('26_17565.txt') as file:
    n, s = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file if i]

data_sum = [[i[0], sum(i[1:-1]), i[-1]] for i in data]

data_sum = sorted(data_sum, key=lambda x: (-x[1]))


prohod = data_sum[:s]

if prohod[-1][1] == data_sum[s][1]:
    while prohod[-1][1] == data_sum[s][1]:
        prohod = prohod[:-1]

half_prohod = [i for i in data_sum if i[1] == data_sum[s][1]]

prohod = sorted(prohod, key=lambda x: (-x[1], -x[-1], -x[0]))

print(len(half_prohod))

print(prohod[-1][0])