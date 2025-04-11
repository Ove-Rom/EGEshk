from ipaddress import *

net = ip_network("192.168.248.176/255.255.255.240", False)

c = 0

for i in net:
    b = bin(int(i))[2:]
    if b.count("0") == b.count("1"):
        c += 1

print(c)