from ipaddress import *

address = ip_address("111.81.192.0")
ip = ip_address("111.81.208.27")

for mask in range(33):
    net = ip_network(f"111.81.208.27/{mask}", False)
    if net.network_address == address and \
            net.broadcast_address != ip:
        print(str(net.netmask).split(".")[2])
        break
