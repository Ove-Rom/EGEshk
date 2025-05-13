# with open("24_9845.txt") as f:
#     data = f.readline()
#
# pat = r"\d?(\D\d)+\D?"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans))
from itertools import permutations, product, groupby
from re import finditer
from string import ascii_uppercase

# with open("24_7600.txt") as f:
#     data = f.readline()
#
# data = data.replace("Q", "S")
# data = data.replace("R", "S")
# data = data.replace("SS", "S S")
# data = data.split()
#
# print(len(max(data, key=len)))

# with open("24_7624.txt") as f:
#     data = f.readline()
#
# data = data.replace("X", "Z")
# data = data.replace("Y", "Z")
# data = data.replace("ZZ", "Z Z")
# data = data.split()
#
# print(len(max(data, key=len)))

# with open("24_8510.txt") as f:
#     data = f.readline()
#
# data = data.replace("N", "P")
# data = data.replace("O", "P")
# while "PP" in data:
#     data = data.replace("PP", "P P")
# data = data.split()
#
# print(len(max(data, key=len)))

# with open("24_4710.txt") as f:
#     data = f.readline()
#
# pat = r"([CDF][AO])+"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans)//2)

# with open("24_6636.txt") as f:
#     data = f.readline()
#
# pat = r"([24][135])+"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans)//2)

# with open("24_6054.txt") as f:
#     data = f.readline()
#
# pat = r"([BC]{2}A)+"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans))

# with open("24_6029.txt") as f:
#     data = f.readline()
#
# pat = r"E?(EF)+F?"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans))

# with open("24_6757.txt") as f:
#     data = f.readline()
#
#
# pat = r"(CFE|FCE)+"
#
# lines = finditer(pat, data)
# ans = []
#
# for i in lines:
#     ans.append(len(i.group()))
# print(max(ans)//3)
#
#
# data = data.replace("CFE", "+")
# data = data.replace("FCE", "+")
#
# ans = []
# for symb, line in groupby(data):
#     if symb == "+":
#         ans.append(len(list(line)))
# print(max(ans))

# with open("24_9791.txt") as f:
#     data = f.readline()
#
# for i in ascii_uppercase[6:]:
#     data = data.replace(i, " ")
#
# data = data.split()
#
# print(len(max(data, key=len)))