data = open("24_10131.txt").read()

# # cA = data.count('A') # 38079
# # cB = data.count('B') # 38519
#
# # data2 = data[:data[data.rfind('A'):].find('B')]
# # print(data2.count('A'), data2.count('B'))
# # print(data[data.find('B'):data.rfind('B')].count('A'))
#
# cordsA = cordsB = []
# cords = set(range(len(data)))
#
# for i in range(len(data)):
#     match data[i]:
#         case 'A':
#             cordsA.append(i)
#         case 'B':
#             cordsB.append(i)
#
# ans = 0
#
# for i in range(len(cordsA) - 1):
#     for j in range(i, len(cordsA) - 1):
#         line = data[cordsA[i - 1] + 1:cordsA[j + 1]]
#         cA = j - i + 1
#         cB = line.count('B')
#         if cA > cB: continue
#         while cA != cB:
#             lB = line.find('B')
#             rB = len(line) - line.rfind('B')
#             if lB < rB:
#                 line = line[lB + 1:]
#             elif lB > rB:
#                 line = line[:lB]
#             else:
#                 line = line[lB + 1:]
#             cB -= 1
#         if cA == cB:
#             ans = max(ans, len(line[cordsA[j+i] - cordsA[i - 1] + 1]))
#

s = data

p = {}
c = mx = 0

for i in range(len(s)):
    match s[i]:
        case 'A': c += 1
        case 'B': c -= 1
    # c += {'A': 1, 'B': -1}.get(s[i], 0)
    if c == 0: mx = i + 1
    mx = max(mx, i - p.get(c, 10 ** 50))
    p[c] = p.get(c, i)

print(mx)
