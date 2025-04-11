from ipaddress import *

for mask in range(32, 1, -1):
    net1 = ip_network(f"211.115.61.154/{mask}", False)
    net2 = ip_network(f"211.115.59.137/{mask}", False)
    if net1.network_address == net2.network_address:
        print(str(net1.netmask).split(".")[2])
        break