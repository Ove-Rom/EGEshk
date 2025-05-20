from re import finditer

from tqdm import tqdm

with open("24_17641.txt") as f:
    data = f.read()

pat = r"(\d+[+*])+(\d+)"
ans = 0
for i in tqdm(finditer(pat, data)):
    s = i.group()
    if eval(s) == 0:
        ans = max(ans, len(s))
    else:
        for l in range(len(s)):
            for r in range(len(s), l, - 1):
                ps = s[l:r].strip("+*")
                if len(ps) < 2: continue
                if ps[1] not in "+*": ps = ps.lstrip("+*0")
                if ps and eval(ps) == 0:
                    ans = max(ans, len(ps))
                    break

print(ans)
