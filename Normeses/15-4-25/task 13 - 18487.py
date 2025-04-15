from ipaddress import *

c = 0

for a in range(256):
    net = ip_network(f"192.214.{a}.184/255.255.255.224", False)
    ip = ip_address(f"192.214.{a}.184")
    if ip != net.network_address:
        for i in net:
            s = f"{int(i):032b}"
            if s.count("1") <= 15: break
        else:
            print(a)
            break