s = "8" * 83

while any(i in s for i in ["111", "88888"]):
    if "111" in s:
        s = s.replace("111", "88", 1)
    else:
        s = s.replace("88888", "8", 1)

print(s)
