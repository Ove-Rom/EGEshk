from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for x in alph[1:35][::-1]:
    num = int(f"6{x}QR{x}", 35) + int(f"{x}59SH", 35) + int(f"PH{x}69YW", 35)
    nums = [0 for i in digits]
    for i in str(num):
        if i in digits:
            nums[int(i)] += 1
    reversed(nums)
    if num % nums.index(max(nums)) ** 2 == 0:
       print(num // nums.index(max(nums)) ** 2)
       break