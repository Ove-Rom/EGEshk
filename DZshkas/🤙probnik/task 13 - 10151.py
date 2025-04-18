from ipaddress import *

ip = ip_address("111.81.192.0")

for mask in range(33):
    net = ip_network(f"111.81.208.27/{mask}", False)
    if net.network_address == ip:
        print(str(net.netmask).split(".")[2])
        break