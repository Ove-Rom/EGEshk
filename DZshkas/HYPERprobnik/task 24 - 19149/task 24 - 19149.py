with open("24_19149.txt") as f:
    data = f.read()

#data = "133+((((123+(123+1+3)+4)+(++123"

data = data.replace("++", " ")
data = data.replace("+)", " ")
data = data.replace("(+", " ")
data = data.replace("+ ", " ")
data = data.replace(" +", " ")
data = data.replace(")(", ") (")
while "()" in data: data = data.replace("()", " ")
for n in "1234":
    data = data.replace(f"{n}(", f"{n} (")
    data = data.replace(f"){n}", f") {n}")
# print(data.count("("), data.count(")"))


ans = []

data = data.split()

for i in range(len(data)):
    opens = [j for j in range(len(data[i])) if data[i][j] == "("]
    for j in opens[::-1]:
        ending = data[i].find(")", j)
        if ending != -1:
            num = str(eval(data[i][j:ending + 1]))
            if int(num) % 2 == 0: ans.append(len(data[i][j:ending + 1]))
            data[i] = data[i][:j] + "1" + str(num.zfill(len(data[i][j:ending + 1]) - 1)) + data[i][ending:]
        else:
            continue
print(max(ans))


# # ans = []
# # print(data)
# #
# # for i in data:
# #     c = 0
# #     bounds = []
# #     for n, j in enumerate(i):
# #         match j:
# #             case "(":
# #                 c += 1
# #             case ")":
# #                 c -= 1
# #         if c == 0 and j in "()": bounds.append(n)
# #         # print(j, c)
# #     if not bounds: bounds = [0, n]
# #     opens = [j for j in range(len(i[:bounds[-1] + 1])) if i[j] == "("]
# #     close = [j for j in range(len(i[:bounds[-1] + 1])) if i[j] == ")"]
# #     print(i)
# #     print(f"bounds = {bounds}")
# #     # print(opens, close)
# #     first = opens[:len(opens) // 2]
# #     last = close[::-1][:len(close) // 2]
# #     print(first, last)
# #     for start, stop in zip(first, last):
# #         line = i[start:stop + 1]
# #         print(line)
# #         if (line.find("(") < line.find(")") and
# #                 all(str.count("(") == str.count(")") for str in line.split("+")) and
# #                 (eval(line) % 2 == 0)):
# #             ans.append(len(line))
# #             break
# #
# # print(max(ans))
