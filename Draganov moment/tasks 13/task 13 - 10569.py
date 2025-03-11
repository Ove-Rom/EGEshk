from ipaddress import ip_network

net = ip_network("10.8.248.131/255.255.224.0", 0)
print(net)