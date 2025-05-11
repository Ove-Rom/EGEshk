from string import ascii_uppercase

from tqdm import tqdm

# with open("24_14502.txt") as f:
#     data = f.read()
#
# ans = []
# l = 0
#
# for r in tqdm(range(len(data))):
#     while len(set(data[l:r])) == 26:
#         l += 1
#     else:
#         ans.append(r - l)
#
# print(min(ans))

# =========================================================================================================

with open('24_14502.txt') as f:
    s = f.read()

symbs = {i: 0 for i in ascii_uppercase}
l = 0
ans = float("inf")

for r in tqdm(range(len(s))):
    symbs[s[r]] += 1
    while 0 not in symbs.values():
        ans = min(r - l + 1, ans)
        symbs[s[l]] -= 1
        l += 1

print(ans)
