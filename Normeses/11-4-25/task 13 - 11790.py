from ipaddress import *

for a in range(16, 25):
    net = ip_network(f"152.65.245.132/{a}", False)
    if all(f"{int(i):032b}"[:17].count("0") >= f"{int(i):032b}"[17:].count("0") for i in net):
        print(a)
        break