from ipaddress import *

for a in range(255, -1, -1):
    net = ip_network(f"217.109.{a}.94/255.255.254.0", False)
    for i in net:
        s = f"{int(i):032b}"
        if not(s[:16].count("0") <= s[16:].count("0")):
            break
    else:
        print(a)
        break