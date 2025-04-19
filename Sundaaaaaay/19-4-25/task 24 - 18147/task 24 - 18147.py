from re import *
from tqdm import tqdm

with open("24_18147.txt") as f:
    data = f.read()

pattern = r"(\d+\+)+\d+"

lines = finditer(pattern, data)

ans = []

for i in tqdm(lines):
    ans.append(eval(i.group()))

print(max(ans))