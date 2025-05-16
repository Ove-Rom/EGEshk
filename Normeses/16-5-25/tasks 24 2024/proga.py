from re import finditer
# with open("24_17535.txt") as f:
#     data = f.read()
#
# data = data.split("CD")
#
# ans = []
#
# for i in range(len(data) - 160):
#     s = "".join(data[i:i+161])
#     ans.append(len(s) + (160*2 + 2))
#
# print(max(ans))

# with open("24_10105.txt") as f:
#     data = f.read().split("T")
#
# ans = []
#
# for i in range(len(data) - 100):
#     s = "".join(data[i:i+101])
#     ans.append(len(s) + 100)
#
# print(max(ans))

# with open("24_12254.txt") as f:
#     data = f.read()
#
# pat = r"(SQ|Q)?(RSQ)+(RS|R)?"
# ans = []
# for i in finditer(pat, data):
#     ans.append(len(i.group()))
#
# print(max(ans))

# with open("24_16388.txt") as f:
#     data = f.read()
#
# pat = r"(LMN|MN|N)?(KLMN)+(KLM|KL|K)?"
#
# ans = []
# for i in finditer(pat, data):
#     ans.append(len(i.group()))
#
# print(max(ans))

with open("24_17563.txt") as f:
    data = f.read()

pat = r"(([1-9]\d*)+[-*])+([1-9]\d*)+"

ans = []
for i in finditer(pat, data):
    ans.append(len(i.group()))

print(max(ans))