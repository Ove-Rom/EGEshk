import math
from fnmatch import fnmatch

for i in range(1157424 + -1157424 % math.gcd(111, 113, 127), 10**8, math.gcd(111, 113, 127)):
    if fnmatch(str(i), "*15*7424"):
        if sum([i % 111 == 0, i % 113 == 0, i % 127 == 0]) == 1:
            match (i % 111 == 0, i % 113 == 0, i % 127 == 0):
                case (True, False, False): print(i, i // 111)
                case (False, True, False): print(i, i // 113)
                case (False, False, True): print(i, i // 127)