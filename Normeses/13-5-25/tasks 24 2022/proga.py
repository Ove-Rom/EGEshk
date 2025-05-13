from itertools import groupby
from re import finditer

# with open("24_1975.txt") as f:
#     data = f.read()
#
# data = data.replace("PP", "P P").split()
#
# print(len(max(data, key=len)))

# with open("24_1866.txt") as f:
#     data = f.read()
#
# data = data.replace("ad", "a d")
# data = data.replace("da", "d a").split()
#
# print(len(max(data, key=len)))

# with open("24_3228.txt") as f:
#     data = f.read()
#
# pat = r"(AC|AB)+"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans)//2)

# with open("24_3584.txt") as f:
#     data = f.readline()
#
# pat = r"(BA|DA)+"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans)//2)

# with open("24_2942.txt") as f:
#     data = f.readline()
#
# pat = r"(AB|AC)+"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans)//2)

# with open("24_4627.txt") as f:
#     data = f.read()
#
# pat = r"(NPO|PNO)+"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans)//3)

# with open("24_4602.txt") as f:
#     data = f.readline()
#
# pat = r"([BCD][AO])+"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans)//2)

# with open("24_4682.txt") as f:
#     data = f.readline()
#
# pat = r"([AE][BCD])+"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans)//2)