from ipaddress import *

c = 0

for a in range(256):
    net = ip_network(f"207.0.{a}.167/255.255.255.192", False)
    for i in net:
        b = f"{int(i):032b}"
        if not (b[:16].count("0") > b[16:].count("0")):
            break
    else:
        c += 1

print(c)
