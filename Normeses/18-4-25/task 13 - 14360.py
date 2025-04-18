from ipaddress import *

ip = ip_address("153.202.16.32")

for mask in range(33):
    net = ip_network(f"153.202.16.37/{mask}", False)
    if net.network_address == ip:
        s = str(net.netmask).split(".")[2:]
        print(sum(int(i) for i in s))