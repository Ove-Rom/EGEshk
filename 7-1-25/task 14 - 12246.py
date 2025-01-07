def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

num = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338

# count = 0
# while num:
#     if num % 9:
#         count += 1
#     num //= 9
#
# print(count)

num = toq(num, 9)

print(sum(i in "12345678" for i in num))