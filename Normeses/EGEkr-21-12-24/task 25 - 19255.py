# for box in range(18579*6, 10000000000, 18579):
#     st = str(box)
#     c1 = st[:2] == "54"
#     c2 = st[3] == '1'
#     c3 = st[5] == '3'
#     c4 = st[-1] == '7'
#     if c1 & c2 & c3 & c4:
#         print(box)
#         break

for num in range(545163597, 10 ** 10 + 1, 18579):
    st = str(num)
    c1 = st[:2] == "54"
    c2 = st[3] == '1'
    c3 = st[5] == '3'
    c4 = st[-1] == '7'
    if c1 & c2 & c3 & c4 and num % 18579 == 0:
        print(num, num // 18579)
'''
Ответ:
545163597 29343
5411932647 291293
5421036357 291783
5451134337 293403
5461538577 293963
5481232317 295023
5491636557 295583
'''
