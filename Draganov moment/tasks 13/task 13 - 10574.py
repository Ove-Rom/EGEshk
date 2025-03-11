from ipaddress import ip_network

c = 0

for mask in range(33):
    net = ip_network(f"158.116.11.146/{mask}", 0)
    if str(net.network_address) == "158.116.0.0":
        c += 1

print(c)