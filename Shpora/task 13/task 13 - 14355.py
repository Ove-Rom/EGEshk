from ipaddress import *

for mask in range(16, 25):
    net = ip_network(f"127.63.67.1/{mask}", False)
    if all(sum(map(int, f"{int(i):b}"[:16])) >= sum(map(int, f"{int(i):b}"[16:])) for i in net):
        print(net.netmask)
        break
