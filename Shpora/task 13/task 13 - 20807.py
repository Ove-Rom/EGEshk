from ipaddress import *

net = ip_network("172.16.192.0/255.255.192.0", False)
c = 0

for i in net:
    s = f"{int(i):032b}"
    c += s.count("1") % 5 != 0

print(c)