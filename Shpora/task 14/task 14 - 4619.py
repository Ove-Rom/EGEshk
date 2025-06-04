def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

n = 343**1515 - 6*49**1520 + 5*49**1510 - 3*7**1530 - 1550
print(toq(n, 7).count("0"))