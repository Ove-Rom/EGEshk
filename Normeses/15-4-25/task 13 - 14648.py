from ipaddress import *

ip = ip_address("218.48.192.56")

adress = ip_address("218.48.192.0")

c = 0

for mask in range(16, 25):
    net = ip_network(f"218.48.192.0/{mask}", False)
    if ip in net and\
            net.num_addresses >= 500 and\
            ip != net.broadcast_address and\
            adress == net.network_address:
        c += 1

print(c)