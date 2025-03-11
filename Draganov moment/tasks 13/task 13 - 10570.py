from ipaddress import ip_network

for mask in range(32, 0, -1):
    net = ip_network(f"154.201.208.17/{mask}", 0)
    if str(net.network_address) == "154.201.192.0":
        print(net.netmask)
        break