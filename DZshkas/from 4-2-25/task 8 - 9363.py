from itertools import permutations
from time import time

hype = time()

count = 0

for i in set(permutations("хочунабюджет")):
    s = "".join(i)
    for j in "оуаюе":
        s = s.replace(j, "x")
    if "xxxxx" not in s:
        count += 1
print(count)
print(time() - hype)