with open("17_2402.txt") as file:
    data = [int(i) for i in file]

def toq(a, q):
    ans = ''
    while a:
        ans += str(a%q)
        a //= q
    return ans[::-1]

mins = []
count = 0

for i in range(len(data) - 2):
    c1 = toq(data[i], 3)[-1] == '2'
    c2 = toq(data[i+1], 3)[-1] == '2'
    c3 = toq(data[i+2], 3)[-1] == '2'
    if c1 or c2 or c3:
        mins.append(min(data[i], data[i+1], data[i+2]))
        count+=1
print(count, sum(mins))