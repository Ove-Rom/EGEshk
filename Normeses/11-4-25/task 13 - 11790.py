from ipaddress import *

for a in range(1, 9):
    # print(int(f"{'1'*a:08}", 2))
    net = ip_network(f"152.65.245.132/255.255.{int(f"{'1'*a:08}", 2)}.0", False)
    if all(f"{int(i):032b}"[:17].count("0") >= f"{int(i):032b}"[17:].count("0") for i in net):
        print(int(f"{'1'*a:08}", 2))
        break