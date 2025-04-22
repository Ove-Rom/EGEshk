from ipaddress import *

ip1 = ip_address("118.187.59.255")
ip2 = ip_address("118.187.65.115")

for mask in range(32, -1, -1):
    net1 = ip_network(f"{ip1}/{mask}", False)
    net2 = ip_network(f"{ip2}/{mask}", False)
    if net1 != net2 and \
            ip1 not in [net1.broadcast_address, net1.network_address] and \
            ip2 not in [net2.broadcast_address, net2.network_address]:
        print(mask)
        break