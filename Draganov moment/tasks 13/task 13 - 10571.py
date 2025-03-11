from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f"122.21.49.91/{mask}", 0)
    if str(net.network_address) == "122.21.48.0":
        print(net)
        break