from ipaddress import *

ip = ip_address("127.63.67.1")

for mask in range(16, 25):
    net = ip_network(f"127.63.67.1/{mask}", False)
    if ip != net.network_address:
        for i in net:
            s = f"{int(i):032b}"
            if not (s[:16].count("1") >= s[16:].count("1")):
                break
        else:
            print(int(str((mask - 16) * "1").zfill(8)[::-1], 2))
            break