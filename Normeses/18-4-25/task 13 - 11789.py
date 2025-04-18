from ipaddress import *

ip = ip_address("99.8.254.232")

for mask in range(16, 25):
    net = ip_network(f"99.8.254.232/{mask}", False)
    if ip != net.network_address and ip != net.broadcast_address:
        for i in net:
            i = f"{int(i):032b}"
            if not (i[:16].count("1") <= i[16:].count("1")):
                break
        else:
            print(net.netmask)
            break