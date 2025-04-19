with open("24_16269.txt") as f:
    data = f.read()

for i in "TUV":
    data = data.replace(f"{i}", " ")

for i in "XYZ":
    while i * 3 in data:
        data = data.replace(f"{i * 3}", f"{i * 2} {i * 2}")

data = data.split()

print(len(max(data, key=len)))
