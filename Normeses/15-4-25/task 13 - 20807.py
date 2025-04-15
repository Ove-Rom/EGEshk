from ipaddress import *

net = ip_network("172.16.192.0/255.255.192.0")

c = 0

for i in net:
    s = f"{int(i):032b}"
    if s.count("1") % 5: c+= 1

print(c)