from ipaddress import *

for a in range(16, 25):
    net = ip_network(f"246.51.128.202/{a}", False)
    for i in net:
        b = f"{int(i):032b}"
        if not (b[:16].count("0") <= b[16:].count("0")):
            break
    else:
        print(f"{int(f"{'1' * (a-16):08}", 2)}")
        break
