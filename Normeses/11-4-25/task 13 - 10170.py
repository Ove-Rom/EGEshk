from ipaddress import *

for mask in range(33):
    net1 = ip_network(f"193.175.175.231/{mask}", False)
    net2 = ip_network(f"193.175.176.118/{mask}", False)
    if net1.network_address != net2.network_address:
        print(str(net1.netmask).split(".")[2])
        break