s = '8' * 45

while "1111" in s or "8888" in s:
    s = s.replace("1111", "88")
    s = s.replace("8888", "11")

print(s)
