from ipaddress import *

ip = ip_address("143.131.211.37")

for mask in range(33):
    net = ip_network(f"{ip}/{mask}", False)
    if ip not in [net.network_address, net.netmask]:
        c = 0
        for i in net:
            s = f"{int(i):032b}"
            if s.count("1") == 10: c += 1
            if c > 15:
                break
        if c == 15:
            print(mask)

