from ipaddress import *

for a in range(255, -1, -1):
    net = ip_network(f"248.112.{a}.35/255.255.255.240", False)
    for i in net:
        s = f"{int(i):032b}"
        if not(s[:16].count("0") <= s[16:].count("0")):
            break
        else:
            print(a)
            exit()