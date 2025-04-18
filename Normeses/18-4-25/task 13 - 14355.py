from ipaddress import *

ip = ip_address("127.63.67.1")

for mask in range(16, 25):
    net = ip_network(f"{ip}/{mask}", False)
    if ip not in [net.network_address, net.broadcast_address]:
        for i in net:
            s = f"{int(i):032b}"
            if not (s[:16].count("1") >= s[16:].count("1")):
                break
        else:
            print(net.netmask)
            break