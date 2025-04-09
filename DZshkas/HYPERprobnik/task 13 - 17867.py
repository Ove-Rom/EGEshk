from ipaddress import *

net = ip_network("172.16.168.0/255.255.248.0", [])

c = 0

for i in net:
    if bin(int(i)).count('1') % 5:
        c += 1

print(c)