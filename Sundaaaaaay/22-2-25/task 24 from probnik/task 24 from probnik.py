data = open("24-2.txt").readline()

data = data.replace("++", " ")
data = data.replace("**", " ")
data = data.replace("*+", " ")
data = data.replace("+*", " ")

# for i in range(10):   # штука для удаления ведущих нулей
#     print(i)
#     while f"*0{i}" in data or f"+0{i}" in data or f" 0{i}" in data:
#         data = data.replace(f"*0{i}", f"*0 {i}")
#         data = data.replace(f"+0{i}", f"+0 {i}")
#         data = data.replace(f" 0{i}", f" 0 {i}")

data = data.split()

ans = []

for i in range(len(data)):
    data[i] = data[i].strip('+').strip('*')
    if eval(data[i]) == 0:
        ans.append(data[i])

print(len(max(ans, key=len)))