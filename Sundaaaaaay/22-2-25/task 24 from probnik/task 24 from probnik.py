data = open("24-2.txt").readline()

data = data.replace("++", " ")
data = data.replace("**", " ")
data = data.replace("*+", " ")
data = data.replace("+*", " ")

# for num in range(10):   # штука для удаления ведущих нулей
#     print(num)
#     while f"*0{num}" in data or f"+0{num}" in data or f" 0{num}" in data:
#         data = data.replace(f"*0{num}", f"*0 {num}")
#         data = data.replace(f"+0{num}", f"+0 {num}")
#         data = data.replace(f" 0{num}", f" 0 {num}")

data = data.split()

ans = []

for i in range(len(data)):
    data[i] = data[i].strip('+').strip('*')
    if eval(data[i]) == 0:
        ans.append(data[i])

print(len(max(ans, key=len)))