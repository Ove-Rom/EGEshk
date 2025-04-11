from ipaddress import *

for mask in range(32, 1, -1):
    net1 = ip_network(f"112.117.107.70/{mask}", False)
    net2 = ip_network(f"112.117.121.80/{mask}", False)
    if net1.network_address == net2.network_address:
        print(str(net1.netmask).split(".")[2])
        break