from ipaddress import *

net = ip_network("156.132.15.138/255.255.252.0", False)

for n, i in enumerate(net):
    if i == ip_address("156.132.15.138"):
        print(n)