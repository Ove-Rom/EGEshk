from ipaddress import *

ip1 = ip_address("216.54.187.235")
ip2 = ip_address("216.54.174.128")

for mask in range(32, -1, -1):
    n1 = ip_network(f"{ip1}/{mask}", False)
    n2 = ip_network(f"{ip2}/{mask}", False)
    if ip1 in n1.hosts() and ip2 in n2.hosts():
        if n1 != n2:
            print(mask)
            break